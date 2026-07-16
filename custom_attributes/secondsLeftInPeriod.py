def secondsLeftInPeriod(shot:dict):
    seconds = 0
    timeRemaining = shot['timeRemaining']
    seconds += int(timeRemaining[0:2])*60
    seconds += int(timeRemaining[3:5])
    return seconds