# this needs to call the api (probably using requests)
# in order to a) accommodate the new 84-game schedule
# and strike-shortened schedules etc and b) to get
# only the valid playoff ids

def allIdsFromRegSeason(season:int):
    ids = []
    for i in range(1, 1313):
        ids.append(f'{season}02{i:04d}')
    return ids
