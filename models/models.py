from joblib import load
from pathlib import Path

doubleppModel = load(Path(__file__).parent/'2pp model.joblib')
ppModel = load(Path(__file__).parent/'pp model.joblib')
evModel = load(Path(__file__).parent/'ev model.joblib')
shModel = load(Path(__file__).parent/'sh model.joblib')
doubleshModel = load(Path(__file__).parent/'2sh model.joblib')

enModel = load(Path(__file__).parent/'pp en model.joblib')
otherenModel = load(Path(__file__).parent/'evsh en model.joblib')