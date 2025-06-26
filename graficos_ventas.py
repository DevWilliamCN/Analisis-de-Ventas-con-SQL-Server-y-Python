import tkinter as tk
from tkinter import ttk
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

# Estilo gráfico
sns.set(style="whitegrid")

# Conexión
def conectar_sql():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=ProyectoVentasSQL;'
        'Trusted_Connection=yes;'
    )

# Centrar ventana
def centrar_ventana(ventana, ancho=1000, alto=600):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Mostrar gráfica productos más vendidos
def mostrar_productos():
    conn = conectar_sql()
    df = pd.read_sql("SELECT * FROM vista_productos_mas_vendidos", conn)
    conn.close()

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(x='total_vendidos', y='nombre_producto', data=df, ax=ax, palette="viridis")
    ax.set_title(" Productos Más Vendidos")
    ax.set_xlabel("Cantidad Vendida")
    ax.set_ylabel("Producto")
    mostrar_grafico(fig)

# Mostrar gráfica compras por cliente
def mostrar_clientes():
    conn = conectar_sql()
    df = pd.read_sql("SELECT * FROM vista_total_compras_por_cliente", conn)
    conn.close()

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(x='Monto_Total', y='Cliente', data=df, ax=ax, palette="rocket")
    ax.set_title("🧍‍♂️ Total de Compras por Cliente")
    ax.set_xlabel("₡ Monto Total")
    ax.set_ylabel("Cliente")
    mostrar_grafico(fig)

# Mostrar gráfico en ventana
def mostrar_grafico(figura):
    for widget in frame_canvas.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(figura, master=frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Interfaz
ventana = tk.Tk()
ventana.title(" Gráficos de Análisis de Ventas")
centrar_ventana(ventana)

# Botones
frame_botones = ttk.Frame(ventana, padding=10)
frame_botones.pack()

ttk.Button(frame_botones, text="📦 Productos más vendidos", command=mostrar_productos).grid(row=0, column=0, padx=10)
ttk.Button(frame_botones, text="🧍 Compras por cliente", command=mostrar_clientes).grid(row=0, column=1, padx=10)

# Canvas de gráficas
frame_canvas = ttk.Frame(ventana)
frame_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

ventana.mainloop()
