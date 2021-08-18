# -*- coding: utf-8 -*-
"""
Created on Wed May  5 00:57:00 2021

@author: Unrated
"""

import sympy
from sympy import *
s = symbols('s')
expr = 10/(s*(s+2)*(s+3)**2)
print(expr)
print()
print(apart(expr))