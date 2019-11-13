import lib601.sm as sm

class Vending(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        if inp == 'quarter':
            return(state + 25, (0, False))
        elif inp == 'cancel':
            return (0, (state, False))
        elif inp == 'dispense':
            if state >= 75:
                return (0, (state - 75, True))
            else:
                return (state, (0, False))

print Vending().transduce(['dispense', 'quarter', 'quarter', 'quarter', 'quarter', 'dispense', 'quarter', 'cancel', 'dispense']) 
                

