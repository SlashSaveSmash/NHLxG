from ast import literal_eval
from pathlib import Path

def allSeasonShotsFromFile(season:int):
    filename = f'shots{season}_{season+1}.txt'
    allShots = []
    with open(Path(__file__).parent.parent/'data'/filename, 'rt') as file:
        for line in file.readlines():
            allShots.append(literal_eval(line))
    return allShots