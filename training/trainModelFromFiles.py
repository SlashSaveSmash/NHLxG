from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame
from joblib import dump
from ast import literal_eval
from validShotFiles import validShotFiles
from modelCriteria import modelCriteria

def trainModelFromFiles():
    scaler = StandardScaler().set_output(transform='pandas')
    model = LogisticRegression(max_iter=1_000_000)
    print('Begun reading files')
    shotSet = []
    files = validShotFiles
    for f in files:
        with open(f, 'rt') as file:
            for line in file.readlines():
                shotSet.append(literal_eval(line))
    
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
    dump(model, 'model.joblib')
    dump(scaler, 'scaler.joblib')