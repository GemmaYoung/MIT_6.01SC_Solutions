import lib601.sig  as sig # Signal
import lib601.ts as ts  # TransducedSignal
import lib601.sm as sm  # SM

######################################################################
##  Make a state machine model using primitives and combinators
######################################################################

def plant(T, initD):
    return sm.Cascade(sm.Gain(-T), sm.FeedbackAdd(sm.R(initD), sm.Wire()))

def controller(k):
    return sm.Gain(k)

def sensor(initD):
    return sm.R(initD)

def wallFinderSystem(T, initD, k):
    return sm.FeedbackSubtract(sm.Cascade(controller(k), plant(T, initD)), sensor(initD))

# Plots the sequence of distances when the robot starts at distance
# initD from the wall, and desires to be at distance 0.7 m.  Time step
# is 0.1 s.  Parameter k is the gain;  end specifies how many steps to
# plot. 

initD = 1.5

def plotD(k, end = 50):
  d = ts.TransducedSignal(sig.ConstantSignal(0.7),
                          wallFinderSystem(0.1, initD, k))
  d.plot(0, end, newWindow = 'Gain '+str(k))

##plotD(0.1)
##plotD(1)
##plotD(2)
##plotD(0)
##plotD(-1)
##plotD(-0.1)
plotD(-2)
##plotD(-10)
##plotD(-12)
plotD(-2.7)
plotD(-3)


