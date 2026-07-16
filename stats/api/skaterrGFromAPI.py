from client import client

def skaterrGFromAPI(skaterId, season):
    allStats = client.stats.skater_stats_summary(f'{season}{season+1}', f'{season}{season+1}')
    for player in allStats:
        if player['playerId'] == skaterId:
            return player['goals']