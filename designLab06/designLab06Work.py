import lib601.sf as sf
import lib601.optimize as optimize
import operator
import lib601.poly as poly

def delayPlusPropModel(k1, k2):
    T = 0.1
    V = 0.1
    
    # Controller:  your code here
##    controller = sf.Sum(sf.Gain(k1), sf.Cascade(sf.Gain(k2), sf.R()))
    controller = sf.SystemFunction(poly.Polynomial([k2, k1]), poly.Polynomial([1]))
    # The plant is like the one for the proportional controller.  Use
    # your definition from last week.
    plant1 = sf.Cascade(sf.Gain(0.1), sf.FeedbackAdd(sf.R(), sf.Gain(1)))
    plant2 = sf.Cascade(sf.Gain(0.1*0.1), sf.FeedbackAdd(sf.R(), sf.Gain(1)))
    # Combine the three parts
    sys = sf.FeedbackSubtract(sf.Cascade(controller, sf.Cascade(plant1, plant2)), sf.Gain(1))
    return sys

## print optimize.optOverLine(lambda x: x*x - x, -1, 1, 100)

# You might want to define, and then use this function to find a good
# value for k2.

# Given k1, return the value of k2 for which the system converges most
# quickly, within the range k2Min, k2Max.  Should call optimize.optOverLine.

def bestk2(k1, k2Min, k2Max, numSteps):
    return optimize.optOverLine(lambda k2: abs(delayPlusPropModel(k1, k2).dominantPole()), k2Min, k2Max, numSteps)

print bestk2(10, -10 ,10, 200)
print bestk2(30, -30 ,30, 600)
print bestk2(100, -100 ,100, 2000)
print bestk2(300, -300 ,300, 6000)

def anglePlusPropModel(k3, k4):
    T = 0.1
    V = 0.1

    # plant 1 is as before
    plant1 = None
    # plant2 is as before
    plant2 = None
    # The complete system
    sys = None
    
    return sys


# Given k3, return the value of k4 for which the system converges most
# quickly, within the range k4Min, k4Max.  Should call optimize.optOverLine.

def bestk4(k3, k4Min, k4Max, numSteps):
    pass
