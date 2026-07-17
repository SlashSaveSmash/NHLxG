from requests import get
from json.decoder import JSONDecodeError

def skaterrGFromAPI(skaterId, season):
    try:
        for i in get(f'https://api-web.nhle.com/v1/player/{skaterId}/landing').json()['seasonTotals']:
            if i['season'] == int(f'{season}{season+1}') and i['leagueAbbrev'] == 'NHL':
                return i['goals']
    except (JSONDecodeError, KeyError):
        return -1
