from collection.allSeasonShotsFromFile import allSeasonShotsFromFile

def teamrGAFromFile(teamId:int, season:int):
    rga = 0
    shots = allSeasonShotsFromFile(season)
    for shot in shots:
        if shot['homeTeamId'] == teamId or shot['awayTeamId'] == teamId:
            if not shot['unusable'] and shot['periodDescriptor']['periodType'] in ['REG', 'OT'] and shot['details']['eventOwnerTeamId'] != teamId:
                try:
                    shot['details']['scoringPlayerId']
                    rga += 1
                except KeyError:
                    pass
    return rga