from client import client
from collection.teamInfoFromId import teamInfoFromId
from collection.prepareShotsFromGameId import prepareShotsFromGameId
from custom_attributes.xGFromShot import xGFromShot

def teamxGFromAPI(teamId, season):
    xg = 0
    ids = []
    for id in client.schedule.team_season_schedule(teamInfoFromId(teamId)['abbreviation'], f'{season}{season+1}')['games']:
        if f'{season}02' in str(id['id']) or f'{season}03' in str(id['id']):
            ids.append(id['id'])
    for id in ids:
        shots = prepareShotsFromGameId(id)
        for shot in shots:
            if not shot['unusable'] and shot['details']['eventOwnerTeamId'] == teamId and shot['periodDescriptor']['periodType'] in ['REG', 'OT']:
                xg += xGFromShot(shot)
    return xg