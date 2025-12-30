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

# 3. Limpieza mínima (ajusta según tu dataset real)
# Ejemplos de operaciones típicas:
# - Normalizar nombres de columnas
df.columns = [c.strip() for c in df.columns]

# - Asegurar tipos de datos básicos
# df["Voyage_Date"] = pd.to_datetime(df["Voyage_Date"], errors="coerce")

# - Eliminar filas totalmente vacías
df = df.dropna(how="all")

# 4. Guardar dataset preparado (aunque sea casi igual al raw)
df.to_csv(MODEL_PATH, index=False)
print("Dataset preparado guardado en:", MODEL_PATH)
