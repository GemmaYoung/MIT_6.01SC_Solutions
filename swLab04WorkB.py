import lib601.poly as poly
import swLab04SignalDefinitions
reload(swLab04SignalDefinitions) # so changes you make in swLab04SignalDefinitions.py will be reloaded
from swLab04SignalDefinitions import *

##StepSignal().plot(-10, 10)

##SummedSignal(ConstantSignal(3.0), StepSignal()).plot(-10, 10)

##ScaledSignal(UnitSampleSignal(), 3).plot(-3, 3)

##R(UnitSampleSignal()).plot(-5, 5)

##Rn(UnitSampleSignal(), 3).plot(-5, 5)

polyR(UnitSampleSignal(),poly.Polynomial([3,2,1])).plot(-5,5)
