from collection.allSeasonShotsFromFile import allSeasonShotsFromFile

def skaterrGFromFile(playerId:int, season:int):
    playerrG = 0
    all_shots = allSeasonShotsFromFile(season)
    for shot in all_shots:
        if not shot['unusable'] and shot['periodDescriptor']['periodType'] in ['REG', 'OT']:
            try:
                if shot['details']['scoringPlayerId'] == playerId:
                    playerrG += 1
            except KeyError:
                pass
    return playerrG