# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 03:26:28 2021

@author: Unrated
"""
import time, numpy as np
from graphene import *
x_list = [-0.98, 1.00, 2.02, 3.03, 4.00]
y_list = [2.44, -1.51, -0.47, 2.54, 7.52]
poly_deg = 2
assert len(x_list) == len(y_list)

power_list = [None]*(1+2*poly_deg)

def power(deg, start=1, end=len(x_list)): # 1 indexed, start and end inclusive
    power_list[deg] = power_list[deg] or sum([i**deg for i in x_list[start-1:end]])
    return power_list[deg]
    
mat = []

def reg(): # this gives a poly_deg+1 square matrix
    asc_num = [i for i in range(1+2*poly_deg)]
    for i in range(len(asc_num)-poly_deg):
        mat.append(list(map(power, asc_num[i:i+poly_deg+1])) + [sum([y_list[j]*x_list[j]**i for j in range(len(x_list))])])
    return mat
reg()
for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] = Fraction(str(mat[i][j]))
ans = GaussianElimination(mat)
print([eval(str(i)) for i in ans])
# print([mat[i]+[y_list[i]] for i in range(len(y_list))])
# print([i for i in range(len(y_list))])
