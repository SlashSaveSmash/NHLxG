from joblib import load
from pathlib import Path

model = load(Path(__file__).parent/'model.joblib')