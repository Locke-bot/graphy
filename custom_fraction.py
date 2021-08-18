import sympy
import numpy as np
from sympy import *
# ar =  np.array([i for i in np.arange(0, 10, step=0.1)])
# print(ar)
class Frat:
    def __init__(self, a, b=None):
        den = 1
        if b is not None:
           den = b
        self.den = den
        self.num = a
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, a):
        self.num, self.den = self.num*a.den + self.den*a.num, self.den*a.den
        self._clean()
        return self
    
    def _sympy_(self):
        return Matrix(self)
    
    def __pow__(self, a):
        self.num **= a
        self.den **= a
        self._clean()
        return self
    
    def __sub__(self, a):
        self.num, self.den = self.num*a.den - self.den*a.num, self.den*a.den
        print(self.num, self.den)
        self._clean()
        return self
    
    def __div__(self, a):
        self.num, self.den = self.num*a.den, self.den*a.num
        self._clean()
        return self
    
    def __mul__(self, a):
        self.num, self.den = self.num*a.num, self.den*a.den
        self._clean()
        return self
    
    def _clean(self):
        x, y = self.num, self.den
        g = 1
        while (x > 0):
            g = x
            x  = y%x
            y = g
        print(g)
        self.num//=g
        self.den//=g
    
    def __str__(self):
        return f'Fraction({self.num}/{self.den})'
    
a = Frat(5, 2)
b = Frat(2, 3)
