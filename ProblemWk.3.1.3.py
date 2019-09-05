from lib601 import sm

class PureFunction(sm.SM):
    def __init__(self, f):
        self.f = f
        self.startState = None
    def getNextValues(self, state, inp):
        return (state, self.f(inp))

s = PureFunction(float)
print s.transduce([3,5])

