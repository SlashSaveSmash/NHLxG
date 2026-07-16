from collection.allSeasonShotsFromFile import allSeasonShotsFromFile

def teamrGFromFile(teamId:int, season:int):
    rg = 0
    shots = allSeasonShotsFromFile(season)
    for shot in shots:
        if shot['typeDescKey'] == 'goal' and shot['periodDescriptor']['periodType'] in ['REG', 'OT'] and shot['details']['eventOwnerTeamId'] == teamId:
            try:
                shot['details']['scoringPlayerId']
                rg += 1
            except KeyError:
                pass
    return rg