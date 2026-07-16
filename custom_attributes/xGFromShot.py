from pandas import DataFrame
from models.models import *
from scalers.scalers import *
from training.modelCriteria import modelCriteria
from custom_attributes.manAdv import manAdv

def xGFromShot(shot:dict):
    emptyNet = False
    situation = manAdv(shot)
    if not situation['team_empty_net'] and not situation['opp_empty_net']:
        if situation['team_skaters'] == situation['opp_skaters']+2: model, scaler = doubleppModel, doubleppScaler
        if situation['team_skaters'] == situation['opp_skaters']+1: model, scaler = ppModel, ppScaler
        if situation['team_skaters'] == situation['opp_skaters']:   model, scaler = evModel, evScaler
        if situation['team_skaters'] == situation['opp_skaters']-1: model, scaler = shModel, shScaler
        if situation['team_skaters'] == situation['opp_skaters']-2: model, scaler = doubleshModel, doubleshScaler
    elif situation['team_empty_net'] and not situation['opp_empty_net']:
        if situation['team_skaters'] > situation['opp_skaters']:  model, scaler = enModel, enScaler
        if situation['team_skaters'] <= situation['opp_skaters']: model, scaler = otherenModel, otherenScaler
    else:
        model, scaler = None, None
        emptyNet = True

    if not emptyNet:
        try:
            shotData = modelCriteria(shot)
            shotData = {key:[value] for key, value in shotData.items()}
            xg = model.predict_proba(scaler.transform(DataFrame(shotData)))[0][1]
        except KeyError:
            xg = 0
    else:
        xg = 1
    return xg
