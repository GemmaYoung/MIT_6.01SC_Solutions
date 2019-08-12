import lib601.sm as sm

class CountingStateMachine(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        return state + 1, self.getOutput(state, inp)

class AlternateZeros(CountingStateMachine):
    def getOutput(self, state, inp):
        if state % 2 == 0:
            return inp
        else:
            return 0


a = AlternateZeros()
print a.transduce([1,2,3,4,5,6])
