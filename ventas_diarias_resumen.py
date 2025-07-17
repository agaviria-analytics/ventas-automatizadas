# ==============================================
# 🐍 Análisis Automatizado de Ventas con Python
# ==============================================
# Simula una exportación de SAP (módulo SD), genera
# un resumen y gráficas de ventas por producto y fecha.
# Autor: Hector A. | Perfil: Analista Jr en formación

# 1. Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 🔹 BLOQUE 1 – Carga de datos
# ==============================
# 2. Cargar hojas desde archivo Excel simulado de SAP
archivo_excel = "datos/ventas_diarias.xlsx"
df_ventas = pd.read_excel(archivo_excel, sheet_name="ventas")
df_productos = pd.read_excel(archivo_excel, sheet_name="productos")
df_fechas = pd.read_excel(archivo_excel, sheet_name="fechas")

# (Opcional) Validación rápida de carga
# print(df_ventas.head())
# print(df_productos.head())
# print(df_fechas.head())

# ==============================
# 🔹 BLOQUE 2 – Limpieza y uniones
# ==============================
# 3. Unir ventas con productos
df_ventas_prod = pd.merge(df_ventas, df_productos, on="id_producto", how="left")

# 4. Unir ventas con fechas
df_ventas_final = pd.merge(df_ventas_prod, df_fechas, on="fecha", how="left")

# 5. Calcular valor total por venta
df_ventas_final["valor_total"] = df_ventas_final["cantidad"] * df_ventas_final["precio_unitario"]

# (Opcional) Validar columnas, tipos y estructura
# print(df_ventas.columns)
# print(df_productos.columns)
# print(df_fechas.columns)
# print(df_ventas.dtypes)
# print(df_fechas.dtypes)

# ==============================
# 🔹 BLOQUE 3 – Análisis de datos
# ==============================
# 6. Total por producto
resumen_producto = df_ventas_final.groupby("nombre_producto")["valor_total"].sum().reset_index()

# 7. Total por fecha
resumen_dia = df_ventas_final.groupby("fecha")["valor_total"].sum().reset_index()

# 8. Producto más vendido
top_producto = resumen_producto.sort_values(by="valor_total", ascending=False).head(1)

# ==============================
# 🔹 BLOQUE 4 – Exportación a Excel
# ==============================
# 9. Crear archivo resumen_ventas.xlsx con varias hojas
with pd.ExcelWriter("resultados/resumen_ventas.xlsx", engine="openpyxl") as writer:
    df_ventas_final.to_excel(writer, sheet_name="Ventas_Completa", index=False)
    resumen_producto.to_excel(writer, sheet_name="Resumen_Producto", index=False)
    resumen_dia.to_excel(writer, sheet_name="Resumen_Fecha", index=False)
    top_producto.to_excel(writer, sheet_name="Top_Producto", index=False)

# ==============================
# 🔹 BLOQUE 5 – Visualización de datos
# ==============================
sns.set_theme(style="whitegrid")

# 10. Gráfico de barras: ventas por producto
plt.figure(figsize=(8, 5))
grafica = sns.barplot(data=resumen_producto, x="nombre_producto", y="valor_total", palette="viridis")

# Etiquetas sobre cada barra
for p in grafica.patches:
    altura = int(p.get_height())
    x = p.get_x() + p.get_width() / 2.
    y = p.get_height()
    grafica.annotate(f'{altura}', (x, y), ha='center', va='bottom', fontsize=10, color='black')

plt.title("Total Vendido por Producto")
plt.xlabel("Producto")
plt.ylabel("Valor Total")
plt.tight_layout()
plt.savefig("graficas/ventas_por_producto_barras.png")
plt.close()

# 11. Gráfico de torta: participación por producto
plt.figure(figsize=(6, 6))
plt.pie(
    resumen_producto['valor_total'],
    labels=resumen_producto['nombre_producto'],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("viridis", len(resumen_producto))
)
plt.title("Participación de Ventas por Producto")
plt.axis('equal')
plt.tight_layout()
plt.savefig("graficas/ventas_por_producto_torta.png")
plt.close()

# ==============================
# ✅ Fin del script
# ==============================
# Este script automatiza todo el análisis y visualización
# para ser usado en portafolios, informes o dashboards.
# Puedes activar los bloques de verificación si deseas ver
# estructuras, columnas o tipos de datos cargados.

