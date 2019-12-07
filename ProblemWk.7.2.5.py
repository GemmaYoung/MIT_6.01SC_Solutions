import operator

def argmin(f, input):
    bestValSoFar = None
    bestArgSoFar = None
    for x in input:
        if bestValSoFar == None or f(x) < bestValSoFar:
            bestValSoFar = f(x)
            bestArgSoFar = x
    return (bestValSoFar, bestArgSoFar)

## print  argmin(lambda x: (x-3)**2, [1,2,3,4])

def argopt(f, input, comp):
    bestValSoFar = None
    bestArgSoFar = None
    for x in input:
        if bestValSoFar == None or comp(f(x), bestValSoFar):
            bestValSoFar = f(x)
            bestArgSoFar = x
    return (bestValSoFar, bestArgSoFar)

print argopt(lambda x: (x-3)**2, [1,2,3,4], operator.lt)
print argopt(lambda x: x[0], [(1,2),(3,4)], operator.lt)
