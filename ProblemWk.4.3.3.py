import lib601.sm as sm

def accumulator(init):
    return sm.FeedbackAdd(sm.Gain(1.0), sm.R(init))

def accumulatorDelay(init):
    return sm.FeedbackAdd(sm.R(init), sm.Gain(1.0))

def accumulatorDelayScaled(init, s):
    return sm.Cascade(sm.FeedbackAdd(sm.R(init), sm.Gain(1.0)), sm.Gain(s))


print accumulator(0).transduce(range(10))
print accumulatorDelay(0).transduce(range(10))
print accumulatorDelayScaled(0, 0.1).transduce(range(10))
