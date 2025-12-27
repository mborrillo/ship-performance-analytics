# KPI Definiciones

## Profit_Per_Voyage

- **Definición**  
  Margen económico de cada viaje, considerando ingresos y costos operativos asociados al mismo.

- **Fórmula**  
  `Profit_Per_Voyage = Revenue_per_Voyage_USD - Operational_Cost_USD`

- **Interpretación**  
  Valores positivos indican viajes rentables; valores negativos indican viajes en pérdida.

---

## Operational_Cost_USD

- **Definición**  
  Costos operativos totales (combustible, tripulación, mantenimiento, etc.) imputados a cada viaje.

- **Origen**  
  Campo original del dataset, utilizado como base para el cálculo de rentabilidad.

---

## Res_Prof/Cost

- **Definición**  
  Indicador derivado que compara el beneficio de un viaje con su estructura de costos operativos.

- **Fórmula**  
  `Res_Prof/Cost = Profit_Per_Voyage - Operational_Cost_USD`

- **Interpretación**  
  Valores muy negativos indican que, incluso tras obtener beneficio, el nivel de costos pesa significativamente sobre el resultado.  
  Este KPI se utiliza de forma exploratoria y se recomienda interpretarlo en conjunto con `Profit_Per_Voyage` y `Operational_Cost_USD`.

---

## Avg_Energy_Efficiency

- **Definición**  
  Eficiencia energética media para un barco, ruta o conjunto de viajes, medida como distancia recorrida por unidad de energía.

- **Fórmula**  
  `Avg_Energy_Efficiency = promedio(Efficiency_nm_per_kWh)`

- **Interpretación**  
  Cuanto mayor es el valor, más distancia recorre la embarcación por kWh consumido, lo que indica mejor desempeño energético.
