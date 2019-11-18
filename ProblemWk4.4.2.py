import lib601.sm as sm

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
        
ltiSm = LTISM([1, 2], [1], [3], [4])
print ltiSm.transduce([1, 2, 3, 4, 5]) 
