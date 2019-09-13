from lib601 import sm

class BA1(sm.SM):
    startState = 0
    def getNextState(self, state, inp):
        if inp != 0:
            return state * 1.02 + inp - 100
        else:
            return state * 1.02

class BA2(sm.SM):
    startState = 0
    def getNextState(self, state, inp):
        return state * 1.01 + inp

ba1= BA1()
ba2= BA2()
maxAccount = sm.Cascade(sm.Parallel(ba1, ba2), sm.PureFunction(max))

print ba1.transduce([0, 100, 10000, -300])
print ba2.transduce([0, 100, 10000, -300])
print maxAccount.transduce([0, 100, 10000, -300])


def switchInput(inp):
    if inp > 3000 or inp < -3000:
        return (inp, 0)
    else:
        return (0, inp)

switchAccount = sm.Cascade(sm.Cascade(sm.PureFunction(switchInput), sm.Parallel2(ba1, ba2)), sm.PureFunction(sum))

print sm.Cascade(sm.PureFunction(switchInput), sm.Parallel2(ba1, ba2)).transduce([0, 100, 10000, -300])
print switchAccount.transduce([0, 100, 10000, -300])
