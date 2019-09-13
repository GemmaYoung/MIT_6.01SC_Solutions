import lib601.sm as sm

class SumTSM(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (state + inp, state + inp)
    def done(self, state):
        return state > 100

a = SumTSM()
#print a.transduce([1,2,3,100,100], verbose = True)


a4 = sm.Repeat(a, n=4)
#print a4.transduce([1,1,100] * 4, verbose = True)

class CountUpTo(sm.SM):
    def __init__(self, upLimit):
        self.upLimit = upLimit
        self.startState = 0
    
    def getNextValues(self, state, inp):
        return (state + 1, state + 1)

    def done(self, state):
        return state >= self.upLimit

m = CountUpTo(3)
##print m.run(n = 20)

def makeSequenceCounter(nums):
    return sm.Sequence([CountUpTo(c) for c in nums])

print makeSequenceCounter([2,5,3]).run(n=20)

