class V2:
    # Delete the pass statement below and insert your own code
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'V2' + str([self.x, self.y])
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def add(self, other):
        sumX = self.x + other.x
        sumY = self.y + other.y
        return V2(sumX, sumY)
    def mul(self, scalar):
        proX = scalar * self.x
        proY = scalar * self.y
        return V2(proX, proY)
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, scalar):
        return self.mul(scalar)
    
