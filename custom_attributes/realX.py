def realX(shot:dict):
    if shot['details']['zoneCode'] == 'O':
        return abs(shot['details']['xCoord'])
    elif shot['details']['zoneCode'] == 'D':
        return -abs(shot['details']['xCoord'])
    elif shot['details']['zoneCode'] == 'N':
        if shot['details']['eventOwnerTeamId'] == shot['homeTeamId']:
            if shot['homeTeamDefendingSide'] == 'right':
                return -abs(shot['details']['xCoord'])
            if shot['homeTeamDefendingSide'] == 'left':
                return abs(shot['details']['xCoord'])
        if shot['details']['eventOwnerTeamId'] == shot['awayTeamId']:
            if shot['homeTeamDefendingSide'] == 'right':
                return abs(shot['details']['xCoord'])
            if shot['homeTeamDefendingSide'] == 'left':
                return -abs(shot['details']['xCoord'])