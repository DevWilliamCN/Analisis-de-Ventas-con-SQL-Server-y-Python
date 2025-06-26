#  Análisis de Ventas con SQL Server y Python (Tkinter + Gráficos)

Este proyecto implementa un sistema completo de análisis, simulación y visualización de datos de ventas conectando **SQL Server** con **Python**, usando interfaces gráficas con **Tkinter** y gráficos con **Seaborn** y **Matplotlib**.

---

##  Funcionalidades

###  1. Simulador de ventas aleatorias
- Genera ventas ficticias con clientes y productos reales
- Inserta registros directamente en la base de datos SQL Server
- Visualiza resultados en tiempo real desde la interfaz

###  2. Clasificador automático de productos más vendidos
- Analiza las ventas de los últimos 15 días
- Clasifica productos como:
  -  Más vendido
  -  Popular
- Guarda y muestra la etiqueta directamente en la tabla `Productos`

###  3. Dashboard gráfico con visualización
- Muestra:
  -  Productos más vendidos
  -  Total de compras por cliente
- Visualización dinámica con botones en ventana centrada

---

##  Tecnologías utilizadas

| Herramienta      | Uso principal                      |
|------------------|------------------------------------|
| Python           | Lógica, interfaces y automatización |
| Tkinter          | Interfaz gráfica (GUI)             |
| SQL Server       | Base de datos relacional           |
| pyodbc           | Conexión Python ↔ SQL Server       |
| pandas           | Manipulación de datos              |
| seaborn / matplotlib | Visualización de datos          |

---

##  Cómo ejecutar el proyecto

### Prerrequisitos
- Tener SQL Server instalado y en ejecución
- Tener una base de datos llamada `ProyectoVentasSQL` con las tablas `Clientes`, `Productos`, `Categorias`, `Ventas`, `DetalleVenta` y vistas necesarias
- Python 3.10 o superior

### Instalar dependencias

```bash
pip install pyodbc pandas matplotlib seaborn
```

### Ejecutar módulos

```bash
python simulador_ventas.py         # Genera ventas aleatorias
python clasificador_productos.py   # Clasifica productos con etiquetas
python graficos_gui.py             # Muestra dashboards gráficos interactivos
```

---

##  Estructura del proyecto

```
ProyectoVentasSQL/
│
├── simulador_ventas.py
├── clasificador_productos.py
├── graficos_gui.py
├── README.md
└── (otros módulos opcionales)
```






