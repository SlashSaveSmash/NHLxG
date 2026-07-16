from pandas import DataFrame
from models.model import model
from scalers.scaler import scaler
from training.modelCriteria import modelCriteria

def xGFromShot(shot:dict):
    try:
        shotData = modelCriteria(shot)
        shotData = {key:[value] for key, value in shotData.items()}
        xg = model.predict_proba(scaler.transform(DataFrame(shotData)))[0][1]
    except KeyError:
        xg = 0
    return xg