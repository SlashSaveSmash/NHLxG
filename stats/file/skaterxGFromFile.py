from collection.allSeasonShotsFromFile import allSeasonShotsFromFile
from custom_attributes.xGFromShot import xGFromShot

def skaterxGFromFile(playerId:int, season:int):
    playerxG = 0
    allShots = allSeasonShotsFromFile(season)
    for shot in allShots:
        if not shot['unusable'] and shot['periodDescriptor']['periodType'] in ['REG', 'OT']:
            try:
                if shot['details']['shootingPlayerId'] == playerId:
                    playerxG += xGFromShot(shot)
            except KeyError:
                if shot['details']['scoringPlayerId'] == playerId:
                    playerxG += xGFromShot(shot)
    return playerxG