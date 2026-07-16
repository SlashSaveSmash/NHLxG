from allIdsFromRegSeason import allIdsFromRegSeason
from prepareShotsFromGameId import prepareShotsFromGameId
from pathlib import Path

def writeSeasonShots(season:int):
    ids = allIdsFromRegSeason(season)
    for id in ids:
        shots = prepareShotsFromGameId(id)
        with open(Path(__file__).parent.parent/'data'/f'shots{season}_{season+1}.txt', 'at') as file:
            for shot in shots:
                file.write(str(shot) + '\n')
        file.close()
