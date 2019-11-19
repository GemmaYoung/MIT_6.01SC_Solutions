"""
Class and some supporting functions for representing and manipulating system functions. 
"""

import math
import lib601.poly as poly
import lib601.util as util
import numpy


class SystemFunction:
    """
    Represent a system function as a ratio of polynomials in R
    """
    
    def __init__(self, numeratorPoly, denominatorPoly):
        self.numerator = numeratorPoly
        self.denominator = denominatorPoly

    def poles(self):
##        return 1.000/numpy.roots(self.denominator.coeffs)
        rCoeffs = self.denominator.coeffs[:]
        rCoeffs.reverse()
        return numpy.roots(rCoeffs)

    def poleMagnitudes(self):
        return [abs(pole) for pole in self.poles()]

    def dominantPole(self):
        return util.argmax(self.poles(), abs)
        

    def __str__(self):
        return 'SF(' + self.numerator.__str__('R') + \
               '/' + self.denominator.__str__('R') + ')'

    __repr__ = __str__


def Cascade(sf1, sf2):
    return SystemFunction(sf1.numerator * sf2.numerator, sf1.denominator * sf2.denominator)

def FeedbackSubtract(sf1, sf2=None):
    return SystemFunction(sf1.numerator * sf2.denominator, sf1.numerator * sf2.numerator + sf1.denominator * sf2.denominator)


