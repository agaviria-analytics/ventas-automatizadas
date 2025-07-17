# 🔹 Análisis Automatizado de Ventas con Python + Excel + Gráficas

Este proyecto simula un escenario real donde los datos de ventas provienen de una exportación desde SAP (módulo SD), y son procesados y visualizados automáticamente con Python para generar un resumen de ventas, gráficas y archivos listos para ser usados en dashboards empresariales (como Power BI).

---

## 🌍 Autor

**Héctor A. Gaviria**
Perfil: Analista de Datos Jr en formación
Portafolio: [agaviria-analytics.github.io](https://agaviria-analytics.github.io)

---

## 🔧 Tecnologías Usadas

* Python 3
* pandas
* matplotlib
* seaborn
* openpyxl

---

## 📚 Estructura del Proyecto

```
.
├── datos/
│   ├── ventas_diarias.xlsx          # Archivo simulado exportado desde SAP
├── resultados/
│   ├── resumen_ventas.xlsx           # Archivo generado con varias hojas (resumen)
├── graficas/
│   ├── ventas_por_producto_barras.png  # Gráfico de barras
│   └── ventas_por_producto_torta.png  # Gráfico de torta
├── ventas_diarias_resumen.py                # Script principal de automatización
└── README.md
```

---

## 📊 Flujo del Script `analisis_ventas.py`

1. **Carga** datos de ventas, productos y fechas desde Excel.
2. **Limpia y une** tablas para generar un dataset final.
3. **Calcula** el valor total vendido por producto y fecha.
4. **Exporta** a un nuevo archivo Excel con múltiples hojas:

   * Ventas completas
   * Resumen por producto
   * Resumen por fecha
   * Top producto
5. **Genera dos gráficos automáticos**:

   * Gráfico de barras
   * Gráfico de torta (participación %)

---

## 🚀 Ideal Para...

* Portafolio profesional como analista jr
* Automatizar reportes semanales de ventas
* Presentar proyectos en entrevistas

---

## 🌐 Publicación

Este proyecto está disponible en:

* [Repositorio GitHub](https://github.com/agaviria-analytics/ventas-automatizadas)
* [Portafolio Web](https://agaviria-analytics.github.io)

---

## 🔄 Actualización Dinámica

Si se actualizan los datos en `ventas_diarias.xlsx`, al ejecutar nuevamente el script:

* Se regeneran las hojas del Excel resumen
* Se actualizan automáticamente los gráficos con los nuevos datos

---

## 🙌 Aporte

Este proyecto fue construido como parte del entrenamiento personal de Héctor para profesionalizarse en el área de datos. Cualquier sugerencia es bienvenida. ¡Gracias por visitar el repositorio!



