from joblib import load
from pathlib import Path

doubleppScaler = load(Path(__file__).parent/'2pp scaler.joblib')
ppScaler = load(Path(__file__).parent/'pp scaler.joblib')
evScaler = load(Path(__file__).parent/'ev scaler.joblib')
shScaler = load(Path(__file__).parent/'sh scaler.joblib')
doubleshScaler = load(Path(__file__).parent/'2sh scaler.joblib')

enScaler = load(Path(__file__).parent/'pp en scaler.joblib')
otherenScaler = load(Path(__file__).parent/'evsh en scaler.joblib')