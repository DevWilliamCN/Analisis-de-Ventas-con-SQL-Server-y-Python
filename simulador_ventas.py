import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
import random
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
def centrar_ventana(ventana, ancho=650, alto=450):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Simulación de ventas
def simular_ventas():
    try:
        cantidad = int(entry_cantidad.get())
        if cantidad <= 0:
            raise ValueError

        conn = conectar_sql()
        cursor = conn.cursor()

        # Obtener IDs de clientes y productos
        clientes = [row[0] for row in cursor.execute("SELECT id_cliente FROM Clientes")]
        productos = list(cursor.execute("SELECT id_producto, precio FROM Productos"))

        resultado = []

        for _ in range(cantidad):
            cliente_id = random.choice(clientes)
            producto_id, precio_unitario = random.choice(productos)
            cantidad_producto = random.randint(1, 5)
            subtotal = round(precio_unitario * cantidad_producto, 2)
            fecha_venta = datetime.now() - timedelta(days=random.randint(0, 30))
            fecha_sql = fecha_venta.strftime('%Y-%m-%d')

            # Insertar venta y obtener ID generado
            cursor.execute(
                "INSERT INTO Ventas (id_cliente, fecha, total) OUTPUT INSERTED.id_venta VALUES (?, ?, ?)",
                cliente_id, fecha_sql, subtotal
            )
            venta_id = cursor.fetchone()[0]
            conn.commit()

            # Insertar detalle
            cursor.execute(
                "INSERT INTO DetalleVenta (id_venta, id_producto, cantidad, subtotal) VALUES (?, ?, ?, ?)",
                venta_id, producto_id, cantidad_producto, subtotal
            )
            conn.commit()

            resultado.append(f"Venta #{venta_id} → Cliente {cliente_id}, Prod {producto_id} x{cantidad_producto} = ₡{subtotal}")

        cursor.close()
        conn.close()

        messagebox.showinfo("Simulación completada", f"✅ Se generaron {cantidad} ventas exitosamente.")
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, "\n".join(resultado))

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresá una cantidad válida (número entero mayor que 0).")
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

# Crear ventana
ventana = tk.Tk()
ventana.title("Simulador de Ventas Aleatorias")
centrar_ventana(ventana)  # Centra la ventana al iniciar

frame = ttk.Frame(ventana, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Cantidad de ventas a generar:").pack()
entry_cantidad = ttk.Entry(frame, width=10)
entry_cantidad.insert(0, "5")
entry_cantidad.pack(pady=5)

ttk.Button(frame, text="🧾 Generar ventas aleatorias", command=simular_ventas).pack(pady=10)

text_resultado = tk.Text(frame, height=15, wrap="word")
text_resultado.pack(fill=tk.BOTH, expand=True)

ventana.mainloop()
