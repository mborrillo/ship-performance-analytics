import pandas as pd
from pathlib import Path

# Rutas
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
RAW_PATH = DATA_DIR / "ship_performance_raw.csv"
MODEL_PATH = DATA_DIR / "ship_performance_model.csv"

DATA_DIR.mkdir(exist_ok=True)

# 1. Carga de datos
df = pd.read_csv(RAW_PATH)

# 2. Exploración básica
print("Shape:", df.shape)
print("Columnas:", df.columns.tolist())
print(df.describe(include="all").T.head())

# 3. Limpieza mínima (Se normalizan nombres de columnas, se aseguran tipos de datos básicos, se eliminan filas vacías)
df.columns = [c.strip() for c in df.columns]

df["Voyage_Date"] = pd.to_datetime(df["Voyage_Date"], errors="coerce")

df = df.dropna(how="all")

# 4. Se guardaa el dataset preparado
df.to_csv(MODEL_PATH, index=False)
print("Dataset preparado guardado en:", MODEL_PATH)
