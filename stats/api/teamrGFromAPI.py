from requests import get
from collection.teamInfoFromId import teamInfoFromId

def teamrGFromAPI(teamId, season):
    teamStats = get(f'https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=seasonId={season}{season+1} and gameTypeId=2').json()['data']
    for team in teamStats:
        if team['teamId'] == teamId:
            return team['goalsFor']
    return -1
