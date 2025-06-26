import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
import pandas as pd
from datetime import datetime, timedelta

# Conexión a SQL Server
def conectar_sql():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=ProyectoVentasSQL;'
        'Trusted_Connection=yes;'
    )

# Centrar ventana
def centrar_ventana(ventana, ancho=850, alto=500):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Función principal: clasifica productos y muestra resultados
def clasificar_productos():
    try:
        conn = conectar_sql()
        cursor = conn.cursor()

        # Fecha límite (últimos 15 días)
        fecha_limite = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')

        # Consulta ventas recientes
        query = f"""
            SELECT p.id_producto, p.nombre_producto, SUM(dv.cantidad) AS total_vendida
            FROM DetalleVenta dv
            JOIN Ventas v ON dv.id_venta = v.id_venta
            JOIN Productos p ON dv.id_producto = p.id_producto
            WHERE v.fecha >= '{fecha_limite}'
            GROUP BY p.id_producto, p.nombre_producto
            ORDER BY total_vendida DESC;
        """

        df = pd.read_sql(query, conn)

        # Clasificación por ranking
        etiquetas = {}
        for idx, row in df.iterrows():
            if idx < 5:
                etiquetas[row["id_producto"]] = " Más vendido"
            elif idx < 10:
                etiquetas[row["id_producto"]] = " Popular"
            else:
                etiquetas[row["id_producto"]] = None

        # Limpiar etiquetas anteriores
        cursor.execute("UPDATE Productos SET etiqueta = NULL")
        conn.commit()

        # Asignar nuevas
        for prod_id, etiqueta in etiquetas.items():
            cursor.execute(
                "UPDATE Productos SET etiqueta = ? WHERE id_producto = ?",
                etiqueta, prod_id
            )
        conn.commit()

        mostrar_resultado(df, etiquetas)
        messagebox.showinfo("Clasificación exitosa", " Etiquetas actualizadas correctamente.")
        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Error crítico", str(e))

# Mostrar resultados en tabla
def mostrar_resultado(df, etiquetas):
    for row in tabla.get_children():
        tabla.delete(row)

    for _, row in df.iterrows():
        prod_id = row["id_producto"]
        etiqueta = etiquetas.get(prod_id, "")
        tabla.insert("", "end", values=(
            prod_id,
            row["nombre_producto"],
            int(row["total_vendida"]),
            etiqueta or ""
        ))

# GUI
ventana = tk.Tk()
ventana.title(" Clasificador Automático de Productos")
centrar_ventana(ventana)  # Centra la ventana

# Botón superior
frame_top = ttk.Frame(ventana, padding=10)
frame_top.pack(fill=tk.X)

ttk.Button(frame_top, text=" Clasificar productos por ventas", command=clasificar_productos).pack()

# Tabla
frame_tabla = ttk.Frame(ventana, padding=10)
frame_tabla.pack(fill=tk.BOTH, expand=True)

tabla = ttk.Treeview(frame_tabla, columns=("ID", "Producto", "Ventas", "Etiqueta"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Producto", text="Nombre del Producto")
tabla.heading("Ventas", text="Ventas (15 días)")
tabla.heading("Etiqueta", text="Etiqueta")

tabla.column("ID", width=50)
tabla.column("Producto", width=300)
tabla.column("Ventas", width=120)
tabla.column("Etiqueta", width=150)

tabla.pack(fill=tk.BOTH, expand=True)

ventana.mainloop()
