from lib601 import sm

class PureFunction(sm.SM):
    def __init__(self, f):
        self.f = f
    def getNextState(self, state, inp):
        return self.f(inp)

s = PureFunction(float)
print s.transduce([3,5])

