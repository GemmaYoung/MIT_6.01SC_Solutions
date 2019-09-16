def mapList(pro, lis):
    return [pro(i) for i in lis]
def sq(x):
    return x*x
print mapList(sq, [1,2,3,4])


def sumAbs(lis):
    return sum(mapList(abs, lis))
print sumAbs([-1, -2, 3, 4])

def mapSquare(pro, lis):
    return [[pro(i, j) for j in lis] for i in lis]
def diff(x, y):
    return x - y
print mapSquare(diff, [1,2,3])
