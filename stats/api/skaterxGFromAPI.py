from client.client import client
from requests import get
from collection.prepareShotsFromGameId import prepareShotsFromGameId
from custom_attributes.xGFromShot import xGFromShot

def skaterxGFromAPI(skaterId, season):
    xg = 0
    gameLog = get(f'https://api-web.nhle.com/v1/player/{skaterId}/game-log/{season}{season+1}/2').json()
    gameIds = [i['gameId'] for i in gameLog['gameLog']]
    for id in gameIds:
        shots = prepareShotsFromGameId(id)
        for shot in shots:
            if shot['periodDescriptor']['periodType'] in ['REG', 'OT']:
                try:
                    if shot['details']['shootingPlayerId'] == skaterId:
                        xg += xGFromShot(shot)
                except KeyError:
                    if shot['details']['scoringPlayerId'] == skaterId:
                        xg += xGFromShot(shot)
    return xg
