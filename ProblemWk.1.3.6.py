class Polynomial:
    # Delete the pass statement below and insert your own code
    def __init__(self, coefficients):
        self.coeffs = [float(c) for c in coefficients]
        self.highExpo = len(self.coeffs) - 1
    def coeff(self, i):
        if i > self.highExpo:
            return 0
        elif i >= 0:
            return self.coeffs[self.highExpo - i]
        else:
            return 'Coefficient invalid!'
                            
    def add(self, other):
        sumCoeffs = []
        i = max(self.highExpo, other.highExpo)
        while i >= 0:
            sumCoeffs += [(self.coeff(i) + other.coeff(i)),]
            i -= 1
        return Polynomial(sumCoeffs)

    def mul(self, other):
        proPoly = Polynomial([])
        exponent = other.highExpo
        for oc in other.coeffs:
            midCoeffs = [sc*oc for sc in self.coeffs]
##            midCoeffs = []
##            for sc in self.coeffs:
##                midCoeffs += [sc * oc,]
            for p in range(exponent):
                midCoeffs += [0,]
            proPoly = proPoly.add(Polynomial(midCoeffs))
            exponent -= 1
        return proPoly

    def __str__(self):
        result = ''
        exponent = self.highExpo
        for sc in self.coeffs:
            if abs(sc) < 1e-9 and self.highExpo == 0:
                return str(sc)
            if abs(sc) < 1e-9 and exponent == 0:
                return result
            if sc > 0 and exponent < self.highExpo:
                result += '+'
            result += str(sc)
            if exponent == 0:
                return result
            result += 'z'
            if exponent > 1:
                result += '**' + str(exponent)
            exponent -= 1
        
    def val(self, v):
        val = 0
        exponent = self.highExpo
        while exponent >= 0:
            val += self.coeff(exponent) * v ** exponent
            exponent -= 1
        return val

    def valHorner(self, v):
        if self.highExpo == 0:
            return self.coeffs[self.highExpo]
        return Polynomial(self.coeffs[:-1]).valHorner(v) * v + self.coeffs[-1]

    def root(self):
        if self.highExpo > 2:
            return 'Order too hight to solve for roots.'
        if self.highExpo == 1:
            return -self.coeff(0)/self.coeff(1)
        if self.highExpo == 2:
            delta = self.coeff(1)**2 - 4*self.coeff(2)*self.coeff(0)
            midVal = -0.5*self.coeff(1)/self.coeff(2)
            if abs(delta) < 1e-9:
                return [midVal,]
            elif delta > 0:
                sqrtDelta = delta**0.5
            else:
                sqrtDelta = complex(delta)**0.5
            return [midVal-0.5*sqrtDelta/self.coeff(2), midVal+0.5*sqrtDelta/self.coeff(2)]

    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)
    def __call__(self, v):
        return self.val(v)
    def __repr__(self):
        return str(self)
        
            
a = Polynomial([1,2,3])
b = Polynomial([3,2,-1])
c = Polynomial([1,-4,4])
