def Balance(n):
    if n == 0:
        return 100.00
    else:
        return Balance(n-1) * (1 + 0.05)

print Balance(4), Balance(24)
