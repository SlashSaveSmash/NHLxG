from requests import get
from collection.teamInfoFromId import teamInfoFromId

def teamrGFromAPI(teamId, season):
    rg = 0
    skaters = get(f'https://api-web.nhle.com/v1/club-stats/{teamInfoFromId(teamId)['abbreviation']}/{season}{season+1}/2').json()['skaters']
    for skater in skaters:
        rg += skater['goals']
    return rg
