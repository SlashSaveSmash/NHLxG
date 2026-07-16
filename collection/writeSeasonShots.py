from allIdsFromRegSeason import allIdsFromRegSeason
from prepareShotsFromGameId import prepareShotsFromGameId

def writeSeasonShots(season:int):
    ids = allIdsFromRegSeason(season)
    for id in ids:
        shots = prepareShotsFromGameId(id)
        with open(f'shots{season}_{season+1}.txt', 'at') as file:
            for shot in shots:
                file.write(str(shot) + '\n')
        file.close()
