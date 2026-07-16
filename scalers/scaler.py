from joblib import load
from pathlib import Path

scaler = load(Path(__file__).parent/'scaler.joblib')