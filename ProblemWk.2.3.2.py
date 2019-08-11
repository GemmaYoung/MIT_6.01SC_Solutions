interest = 0.12
fee = 0.04
class AccountDollars:
    def __init__(self, initBalance):
        self.balance = initBalance
    def depositDollars(self, deposit):
        return self.balance * (1 + interest) + deposit - fee

class AccountPounds(AccountDollars):
    def __init__(self, initBalancePounds):
        AccountDollars.__init__(self, initBalancePounds * 2)
    def depositPounds(self, depositPounds):
        return AccountDollars.depositDollars(self, depositPounds * 2) / 2

x = AccountDollars(2)
print x.depositDollars(3)

y = AccountPounds(1)
print y.depositPounds(1.5)

        

