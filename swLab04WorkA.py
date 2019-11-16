import lib601.poly as poly
import lib601.sig
from lib601.sig import *

## You can evaluate expressions that use any of the classes or
## functions from the sig module (Signals class, etc.).  You do not
## need to prefix them with "sig."


step1 = ScaledSignal(Rn(StepSignal(),3), 3.0)
step1a = polyR(StepSignal(), poly.Polynomial([3, 0, 0, 0]))

##step1.plot(-10, 10)
##step1a.plot(-10, 10)

step2 = ScaledSignal(Rn(StepSignal(),7), -3.0)
##step2.plot(0, 20)

stepUpDown = SummedSignal(step1, step2)
##stepUpDown.plot(0, 20)

stepUpDownPoly = polyR(UnitSampleSignal(), poly.Polynomial([5.0, 0, 3.0, 0, 1.0, 0]))
stepUpDownPoly.plot(0,10)









