# Ship Performance Dashboard – Documentación de apoyo

Este documento describe la estructura y uso del dashboard Ship Performance.

## Enlace al dashboard

- [Ship Performance Dashboard](https://lookerstudio.google.com/u/1/reporting/e481b79a-fb1e-4f0a-a4a2-58e08fa082f4/page/p_m1xbbza0od)

## Páginas del dashboard

### 1. Home / Introducción

- Presenta el contexto del proyecto, objetivos y breve explicación de las páginas siguientes.  
- Incluye textos guía sobre cómo navegar el dashboard y qué tipo de decisiones soporta.

### 2. Resumen general

- Muestra KPIs globales: `Profit_Per_Voyage`, `Operational_Cost_USD` y `Avg_Energy_Efficiency` por barco y periodo.  
- Permite identificar rápidamente qué barcos aportan mayor o menor rentabilidad.

### 3. Análisis por categorías

- Desglosa los KPIs por dimensiones como tipo de barco, ruta o región.  
- Ayuda a detectar qué categorías concentran mayor costo o mejor eficiencia.

### 4. Impacto climático

- Relaciona condiciones climáticas con la rentabilidad y eficiencia energética.  
- Permite analizar cómo cambian los resultados bajo distintos escenarios de clima.

### 5. Patrones estacionales

- Analiza comportamiento de los KPIs por mes, trimestre o temporada.  
- Útil para identificar periodos sistemáticamente más costosos o menos rentables.

### 6. Detalles específicos

- Tabla de detalle a nivel viaje, con filtros por barco, ruta, fecha y clima.  
- Ideal para análisis granular de outliers o viajes con desempeño atípico.

### 7. Glosario

- Recopila definiciones de campos y KPIs visibles en el dashboard.  
- Alineado con los documentos `docs/data_dictionary.md` y `docs/kpi_definitions.md`.

## Ejemplos de uso

- Identificar el barco menos rentable en el último año filtrando por periodo y ordenando por `Profit_Per_Voyage`.  
- Analizar el impacto del clima comparando `Profit_Per_Voyage` y `Avg_Energy_Efficiency` entre distintas condiciones climáticas.  
- Estudiar patrones estacionales de costos operativos para planificar rutas o mantenimiento.

