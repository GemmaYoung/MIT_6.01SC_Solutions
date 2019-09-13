import lib601.sm as sm

def neg(inp):
    return not(inp)

negate = sm.PureFunction(neg)

alternating = sm.Feedback(sm.Cascade(negate, sm.Delay(True)))

print alternating.transduce([1,2,3,True,False])
