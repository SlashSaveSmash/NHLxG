from collection.allSeasonShotsFromFile import allSeasonShotsFromFile
from custom_attributes.xGFromShot import xGFromShot

def teamxGAFromFile(teamId:int, season:int):
    xga = 0
    shots = allSeasonShotsFromFile(season)
    for shot in shots:
        if shot['homeTeamId'] == teamId or shot['awayTeamId'] == teamId:
            if not shot['unusable'] and shot['periodDescriptor']['periodType'] in ['REG', 'OT'] and shot['details']['eventOwnerTeamId'] != teamId:
                xga += xGFromShot(shot)
    return xga