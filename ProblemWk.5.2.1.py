import lib601.sf as sf

def controllerSF(k):
    return sf.Gain(k)

def plantSF(T):
    return sf.Cascade(sf.Gain(-T), sf.FeedbackAdd(sf.R, sf.Gain(1)))

def sensorSF():
    return sf.R

def wallFinderSystemSF(T, k):
    return sf.FeedbackSubtract(sf.Cascade(controllerSF(k), plant(T)), sensorSF())
