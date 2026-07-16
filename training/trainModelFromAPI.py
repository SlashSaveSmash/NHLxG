from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from nhlpy.http_client import ResourceNotFoundException
from collection.allIdsFromRegSeason import allIdsFromRegSeason
from pandas import DataFrame
from joblib import dump
from modelCriteria import modelCriteria
from collection.prepareShotsFromGameId import prepareShotsFromGameId
from pathlib import Path

def trainModelFromAPI():
    scaler = StandardScaler().set_output(transform='pandas')
    model = LogisticRegression(max_iter=1_000_000)
    print('Begun API calls')
    shotSet = []
    for i in range(2019, 2026):
        ids = allIdsFromRegSeason(i)
        for id in ids:
            try:
                shots = prepareShotsFromGameId(id)
                for shot in shots:
                    shotSet.append(shot)
            except ResourceNotFoundException:
                pass
    
    print('Extrapolating for model')
    trainingData = []
    for shot in shotSet:
        try:
            shotData = modelCriteria(shot)
            shotData['goal'] = 1 if shot['typeDescKey'] == 'goal' else 0
            trainingData.append(shotData)
        except KeyError:
            pass

    print('Starting to train')
    dataFrame = DataFrame(trainingData)
    x = dataFrame.drop(columns='goal')
    y = dataFrame['goal']

    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
    xTrainScaled = scaler.fit_transform(xTrain)

    model.fit(xTrainScaled, yTrain)
    dump(model, Path(__file__).parent.parent/'models'/'model.joblib')
    dump(scaler, Path(__file__).parent.parent/'scalers'/'scaler.joblib')
