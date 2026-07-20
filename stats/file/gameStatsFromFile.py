from collection.allSeasonShotsFromFile import allSeasonShotsFromFile
from custom_attributes.xGFromShot import xGFromShot

def gameStatsFromFile(gameId):
    homerG = 0
    homexG = 0
    homeSOG = 0
    homeSO = 0

    awayrG = 0
    awayxG = 0
    awaySOG = 0
    awaySO = 0

    shots = [i for i in allSeasonShotsFromFile(str(gameId)[0:4]) if i['gameId'] == gameId]
    for shot in shots:
        homeId = shot['homeTeamId']
        awayId = shot['awayTeamId']
        if shot['periodDescriptor']['periodType'] in ['REG', 'OT']:
            if shot['details']['eventOwnerTeamId'] == shot['homeTeamId']:
                homeSOG += 1
                homexG += xGFromShot(shot)
                if shot['typeDescKey'] == 'goal':
                    homerG += 1
            if shot['details']['eventOwnerTeamId'] == shot['awayTeamId']:
                awaySOG += 1
                awayxG += xGFromShot(shot)
                if shot['typeDescKey'] == 'goal':
                    awayrG += 1
        if shot['periodDescriptor']['periodType'] == 'SO':
            if shot['details']['eventOwnerTeamId'] == shot['homeTeamId'] and shot['typeDescKey'] == 'goal':
                homeSO += 1
            if shot['details']['eventOwnerTeamId'] == shot['awayTeamId'] and shot['typeDescKey'] == 'goal':
                awaySO += 1
    
    return {
        'homeId': homeId,
        'homexG': float(homexG),
        'homerG': homerG,
        'homeSOG': homeSOG,
        'homeSO': homeSO,
        'awayId': awayId,
        'awayxG': float(awayxG),
        'awayrG': awayrG,
        'awaySOG': awaySOG,
        'awaySO': awaySO
    }
