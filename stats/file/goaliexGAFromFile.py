from collection.allSeasonShotsFromFile import allSeasonShotsFromFile
from custom_attributes.xGFromShot import xGFromShot

def goaliexGAFromFile(playerId:int, season:int):
    xga = 0
    shots = allSeasonShotsFromFile(season)
    for shot in shots:
        if not shot['unusable'] and shot['periodDescriptor']['periodType'] in ['REG', 'OT']:
            try:
                if shot['details']['goalieInNetId'] == playerId:
                    xga += xGFromShot(shot)
            except KeyError:
                pass
    return xga