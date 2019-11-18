import lib601.sm as sm
import lib601.sig as sig

def dotProd(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    if len(a) != len(b):
        print 'dotProd mismatch error ' + str(len(a)) + ' != ' + str(len(b))
    return sum([ai*bi for (ai,bi) in zip(a,b)]) 

class LTISM(sm.SM):
    def __init__(self, dCoeffs, cCoeffs,
                 previousInputs = [], previousOutputs = []):
        self.dCoeffs = dCoeffs
        self.cCoeffs = cCoeffs
        self.startState = (previousInputs, previousOutputs)

    def getNextValues(self, state, inp):
        (inputs, outputs) = state
        o = inp * self.dCoeffs[0] + dotProd(self.cCoeffs, outputs) + dotProd(self.dCoeffs[1:], inputs)
        newInputs = inputs[:-1] + [inp]
        newOutputs = outputs[:-1] + [o]
        return ((newInputs, newOutputs), o)

class TransducedSignal(sig.Signal):
    def __init__(self, s, m):
        self.s = s
        self.m = m

    def sample(self, n):
        if n < 0:
            return 0
        else:
            self.m.start()
            for j in range(n + 1):
                o = self.m.step(self.s.sample(j))
        return o


depositTime0 = sig.ScaledSignal(sig.UnitSampleSignal(),100)
depositTime20 = sig.SummedSignal(depositTime0, sig.Rn(depositTime0, 20))
inputSignal = sig.SummedSignal(depositTime20, sig.Rn(depositTime0, 50))
accountSM = LTISM([1], [0.990], [], [0])
balanceSignal = TransducedSignal(inputSignal, accountSM)

for n in [0, 10, 20, 30, 40, 50, 60]:
    print balanceSignal.sample(n)








                
            
