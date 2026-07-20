from httpx import ConnectError, ConnectTimeout, ReadTimeout
from time import sleep
from custom_attributes.realX import realX
from custom_attributes.secondsLeftInPeriod import secondsLeftInPeriod
from client import client
from nhlpy.http_client import ServerErrorException

def prepareShotsFromGameId(gameId:int):
    connected = False
    while not connected:
        try:
            allInformation = client.game_center.play_by_play(gameId)
            connected = True
        except (ReadTimeout, ConnectError, ConnectTimeout, ServerErrorException):
            print('Connection issue, waiting 5 seconds')
            sleep(5)
        except ResourceNotFoundException:
            pass
    lastShotTime = -1
    allPlays = allInformation['plays']
    for i in range(len(allPlays)):
        if allPlays[i]['typeDescKey'] in ['goal', 'shot-on-goal']:
            try:
                allPlays[i]['gameId'] = gameId
                allPlays[i]['homeTeamId'] = allInformation['homeTeam']['id']
                allPlays[i]['awayTeamId'] = allInformation['awayTeam']['id']
                allPlays[i]['realX'] = realX(allPlays[i])
                allPlays[i]['previousEvent'] = allPlays[i-1]['typeDescKey']
                allPlays[i]['timeSinceLastShot'] = max(lastShotTime - secondsLeftInPeriod(allPlays[i]), -1)
                lastShotTime = secondsLeftInPeriod(allPlays[i])
                allPlays[i]['unusable'] = False
            except KeyError:
                allPlays[i]['unusable'] = True
    
    return [i for i in allPlays if i['typeDescKey'] in ['goal', 'shot-on-goal']]
