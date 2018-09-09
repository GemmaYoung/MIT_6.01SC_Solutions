def evenSquares(L):
    return [e**2 for e in L if e%2== 0]

##print evenSquares([])
##print evenSquares([1, 2, 3])
##print evenSquares([-2, -2.2, 0, 78.7])

def sumAbsProd(L1, L2):
    return sum([abs(e1 * e2) for e1 in L1 \
                  for e2 in L2])

print sumAbsProd([2,-3], [4,-5])
