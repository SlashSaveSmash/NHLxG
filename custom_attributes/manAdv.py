def manAdv(shot:dict):
    def interpretCode(code:str, homeTeam:bool):
        type = None
        teamSkaters = None
        oppSkaters = None
        teamEmptyNet = None
        oppEmptyNet = None
        if homeTeam:
            if code[0] == '1':
                oppEmptyNet = False
            elif code[0] == '0':
                oppEmptyNet = True
            oppSkaters = int(code[1])
            teamSkaters = int(code[2])
            if code[3] == '1':
                teamEmptyNet = False
            elif code[3] == '0':
                teamEmptyNet = True
        elif not homeTeam:
            if code[3] == '1':
                oppEmptyNet = False
            elif code[3] == '0':
                oppEmptyNet = True
            oppSkaters = int(code[2])
            teamSkaters = int(code[1])
            if code[0] == '1':
                teamEmptyNet = False
            elif code[0] == '0':
                teamEmptyNet = True
        if teamSkaters > oppSkaters:
            type = 'power_play'
        elif teamSkaters < oppSkaters:
            type = 'short_handed'
        elif teamSkaters == oppSkaters and teamSkaters != None:
            type = 'even'
        return {
            'type': type,
            'team_empty_net': teamEmptyNet,
            'team_skaters': teamSkaters,
            'opp_skaters': oppSkaters,
            'opp_empty_net': oppEmptyNet
        }
    situationCode = shot['situationCode']
    homeTeamId = shot['homeTeamId']
    awayTeamId = shot['awayTeamId']
    if shot['details']['eventOwnerTeamId'] == homeTeamId:
        return interpretCode(situationCode, True)
    elif shot['details']['eventOwnerTeamId'] == awayTeamId:
        return interpretCode(situationCode, False)