import pyodbc
import pandas as pd

# Configura tu conexión
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=ProyectoVentasSQL;'
    'Trusted_Connection=yes;'
)

# Crea un cursor para ejecutar SQL
cursor = conexion.cursor()

# Ejemplo: leer productos más vendidos desde la vista
consulta = "SELECT * FROM vista_productos_mas_vendidos"
df = pd.read_sql(consulta, conexion)

# Mostrar resultados
print("\n📦 Productos más vendidos:\n")
print(df)

# Cerrar conexión
conexion.close()
