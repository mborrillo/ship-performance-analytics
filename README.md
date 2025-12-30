# Ship Performance Analytics

Proyecto de analítica de rendimiento económico y operativo de viajes marítimos, usando un dataset público y un dashboard interactivo construido en Looker Studio. El objetivo es apoyar la toma de decisiones sobre rentabilidad, costos y eficiencia energética de una flota.

## Contexto

Las operaciones de shipping implican altos costos operativos y exposición a factores externos como clima, rutas y estacionalidad. Este proyecto analiza viajes de una flota para responder preguntas clave, como:

- ¿Qué barcos y viajes son más o menos rentables?
- ¿Cómo impactan los costos operativos en el margen de cada viaje?
- ¿Qué tan eficiente es energéticamente cada barco?
- ¿Existen patrones estacionales o por condiciones climáticas que afecten el desempeño?

## Dataset

- **Origen**: dataset público de rendimiento de viajes marítimos (Kaggle).  
- **Archivo original**: `data/ship_performance_raw.csv`.  
- **Archivo preparado/modelado** (opcional): `data/ship_performance_model.csv`.  

Campos principales (no exhaustivo):

- `Revenue_per_Voyage_USD`: ingresos por viaje en USD.  
- `Operational_Cost_USD`: costos operativos totales por viaje en USD.  
- `Efficiency_nm_per_kWh`: millas náuticas por kWh consumido.  
- Identificadores de barco, fechas, rutas y condiciones climáticas.

El detalle completo de campos y tipos está en `docs/data_dictionary.md`.

## KPIs principales

Definiciones resumidas (detalle completo en `docs/kpi_definitions.md`):

- **Profit_Per_Voyage**  
  - Fórmula: `Profit_Per_Voyage = Revenue_per_Voyage_USD - Operational_Cost_USD`.  
  - Uso: medir la rentabilidad económica de cada viaje.

- **Operational_Cost_USD**  
  - Campo original del dataset, utilizado como referencia de estructura de costos.

- **Res_Prof/Cost**  
  - Fórmula: `Res_Prof/Cost = Profit_Per_Voyage - Operational_Cost_USD`.  
  - Uso: cuantificar la diferencia entre el beneficio del viaje y la estructura de costos.  
  - Nota: este KPI es menos estándar; se explica su interpretación en `docs/kpi_definitions.md`.

- **Avg_Energy_Efficiency**  
  - Fórmula: promedio de `Efficiency_nm_per_kWh` para el nivel de agregación analizado (barco, ruta, periodo).  
  - Uso: evaluar la eficiencia energética de la flota.

## Flujo de trabajo

1. El dataset original se almacena en `data/ship_performance_raw.csv`.
2. En `notebooks/01_data_preparation.py` se realiza la preparación básica y se genera `data/ship_performance_model.csv`.
3. En `notebooks/02_kpi_calculation.py` se calculan los KPIs de negocio y se genera `data/ship_performance_with_kpis.csv`.
4. El archivo enriquecido se conecta a Looker Studio como fuente del dashboard.
5. En `dashboard/screenshots.md` se documentan las páginas del dashboard con capturas de pantalla.

## Dashboard en Looker Studio

- **Enlace al dashboard**:  
  - [Ship Performance Dashboard](https://lookerstudio.google.com/u/1/reporting/e481b79a-fb1e-4f0a-a4a2-58e08fa082f4/page/p_m1xbbza0od)

Páginas principales:

- **Home / Introducción**: contexto del proyecto, objetivos de análisis y explicación de la narrativa del dashboard.  
- **Resumen general**: visión global de rentabilidad, costos y eficiencia por barco y periodo.  
- **Análisis por categorías**: comparación por tipo de barco, ruta, u otras dimensiones clave.  
- **Impacto climático**: relación entre condiciones climáticas y performance económico y energético.  
- **Patrones estacionales**: análisis de variaciones por mes, trimestre u otras ventanas temporales.  
- **Detalles específicos**: tabla de detalle a nivel viaje para análisis granular.  
- **Glosario**: definiciones de métricas, KPIs y términos técnicos usados en el dashboard.

Capturas de ejemplo se encuentran en `dashboard/screenshots.md`.

## Casos de uso

Ejemplos de preguntas que se pueden responder con el dashboard:

- ¿Qué barcos muestran menor `Profit_Per_Voyage` en el último año y qué viajes explican ese desempeño?  
- ¿Qué rutas concentran los mayores `Operational_Cost_USD` y cómo afecta eso a la rentabilidad?  
- ¿Cómo varía la `Avg_Energy_Efficiency` por barco y por temporada?  
- ¿En qué condiciones climáticas se observa mayor caída en el margen de los viajes?  
- ¿Qué viajes individuales presentan comportamientos anómalos (margen muy alto o muy bajo)?

## Alcance y Limitaciones

- El dataset es estático, no se trata de un análisis en tiempo real.
- El dataset cubre un periodo acotado (06/2023 a 06/2024), por lo que las conclusiones se restringen a este intervalo únicamente.
- Las situaciones climáticas fueron agrupadas según la clasificación original del dataset, lo que puede simplificar la realidad operativa.
- No se incluyen métricas de emisiones, cumplimiento normativo ni utilización de capacidad, que son relevantes en operaciones reales de flota.
- El modelo no incorpora costos financieros, ni ingresos complementarios (por ejemplo, recargos o descuentos específicos), por lo que la rentabilidad es operativa, no total.

## Cómo reproducir el proyecto

1. Clonar este repositorio:
git clone https://github.com/mborrillo/ship-performance-analytics.git
cd ship-performance-analytics

2. Colocar el dataset original en `data/ship_performance_raw.csv` (o seguir las instrucciones para descargarlo desde la fuente original).  
3. Conectar el archivo resultante a Looker Studio y replicar la estructura de páginas descrita en `dashboard/README_dashboard.md`.

## Licencia y créditos

- Los datos pertenecen a su fuente original (Kaggle).  
- Parte de los textos descriptivos y glosario se elaboraron con ayuda de modelos de lenguaje IA, y han sido revisados manualmente antes de su publicación.


