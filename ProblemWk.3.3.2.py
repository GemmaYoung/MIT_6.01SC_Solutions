def recursiveRef(nested, lis):
    if lis == []:
        return nested
    else:
        return recursiveRef(nested[lis[0]], lis[1:])


nested = [[[1, 2],3],[4,[5, 6]],7,[8, 9, 10]]
print recursiveRef(nested, [3, 1])
print recursiveRef(nested, [1, 1, 0])
print recursiveRef(nested, [1, 1])
