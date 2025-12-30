import pandas as pd
from pathlib import Path

# Rutas
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = DATA_DIR / "ship_performance_model.csv"

df = pd.read_csv(MODEL_PATH)

# Cálculo de KPIs
df["Profit_Per_Voyage"] = df["Revenue_per_Voyage_USD"] - df["Operational_Cost_USD"]

# KPI exploratorio tal como lo definiste
df["Res_Prof/Cost"] = df["Profit_Per_Voyage"] - df["Operational_Cost_USD"]

# Eficiencia energética (si no viene ya agregada)
# Si Efficiency_nm_per_kWh ya está a nivel viaje, no hace falta recalcular.
# Aquí simplemente nos aseguramos de que exista.
assert "Efficiency_nm_per_kWh" in df.columns, "Falta Efficiency_nm_per_kWh en el dataset"

# Guardar dataset enriquecido con KPIs
ENRICHED_PATH = DATA_DIR / "ship_performance_with_kpis.csv"
df.to_csv(ENRICHED_PATH, index=False)
print("Dataset con KPIs guardado en:", ENRICHED_PATH)
