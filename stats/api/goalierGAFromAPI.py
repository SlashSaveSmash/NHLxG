from requests import get
from json.decoder import JSONDecodeError

def goalierGAFromAPI(goalieId, season):
    try:
        for i in get(f'https://api-web.nhle.com/v1/player/{goalieId}/landing').json()['seasonTotals']:
            if i['season'] == int(f'{season}{season+1}') and i['leagueAbbrev'] == 'NHL':
                return i['goalsAgainst']
            return -1
    except (JSONDecodeError, KeyError):
        return -1
