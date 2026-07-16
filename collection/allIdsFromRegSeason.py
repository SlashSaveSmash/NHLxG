def allIdsFromRegSeason(season:int):
    ids = []
    for i in range(1, 1313):
        ids.append(f'{season}02{i:04d}')
    return ids