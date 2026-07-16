from collection.allSeasonShotsFromFile import allSeasonShotsFromFile
from custom_attributes.xGFromShot import xGFromShot

def teamxGFromFile(teamId:int, season:int):
    xg = 0
    shots = allSeasonShotsFromFile(season)
    for shot in shots:
        if not shot['unusable'] and shot['periodDescriptor']['periodType'] in ['REG', 'OT'] and shot['details']['eventOwnerTeamId'] == teamId:
            xg += xGFromShot(shot)
    return xg