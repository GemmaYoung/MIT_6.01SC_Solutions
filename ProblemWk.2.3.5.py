def slowMod(a, b):
    if a - b < 0:
        return a
    else:
        return slowMod(a - b, b)

print slowMod(5,2)
print slowMod(6,2)
print slowMod(8,3)
print slowMod(4,6)
