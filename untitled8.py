# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:29:20 2021

@author: Unrated
"""


from anothercv import *
from fractions import Fraction
import matplotlib.pyplot as plt
# import os
# print(os.path.exists('shitfaced.png'))
coord = get_cordinates(r'shitfaced.png')
# print(len(coord[1]), len(coord[1]))
# print(list(map(list, zip([Fraction(i) for i in coord[0][::4]], [Fraction(i) for i in coord[1][::4]]))))
x = coord[0]
y = coord[1]
print(x)
print('====')
print(y)
# print(sorted([Fraction(i, j) for i, j in zip(x, y)]))
plt.plot(coord[0], coord[1])
plt.show()