def warehouseProcess(totals, transaction):
    (rOrS, commo, num) = transaction
    if rOrS == 'receive':
        totals[commo] += num
    else:
        if not commo in totals or totals[commo] <= num:
            return 'Failure'
        totals[commo] -= num
    return 'Success'


class Warehouse:
    def __init__(self, dic = {'a':10, 'b':20, 'c':0}):
        self.totals = dic
    def process(self, transaction):
         return warehouseProcess(self.totals, transaction)
    def lookup(self, commodity):
        return self.totals[commodity]

w = Warehouse()
print w.process(('receive', 'a', 10))
print w.process(('ship', 'a', 7))
print w.lookup('a')
print w.process(('ship', 'b', 23))
print w.lookup('b')
