from collection.allSeasonShotsFromFile import allSeasonShotsFromFile

def goalierGAFromFile(playerId:int, season:int):
    rga = 0
    shots = allSeasonShotsFromFile(season)
    for shot in shots:
        if shot['periodDescriptor']['periodType'] in ['REG', 'OT'] and shot['typeDescKey'] == 'goal':
            try:
                if shot['details']['goalieInNetId'] == playerId:
                    rga += 1
            except KeyError:
                pass
    return rga