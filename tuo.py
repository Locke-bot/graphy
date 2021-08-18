# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:45:03 2021

@author: Unrated
"""
import graphene, time
from benchmark import prepare_lists
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
from decimal import Decimal
import random, itertools
from fractions import Fraction
from scipy import linalg
import numpy as np
from sympy import *
import mpmath
import string, sys


def preemptZero(x):
    if x == 0 and end < 0: # can't raise zero to negative power
        x = 1e-15
    return x

def calc(x):
    return graphene.Fraction('1.1')*graphene.Fraction(str(Decimal(x**2.1))) - graphene.Fraction('31.000000001')*graphene.Fraction(str(x**4)) + graphene.Fraction('4')*graphene.Fraction(str(x.numerator), str(x.denominator)) + graphene.Fraction('5')
    
start, startloop = 6.4, 150
end, endloop = 0, 86
step = Fraction(1, 10) # don't give it input as a float, ever.
steploop = Fraction(1)


all_array = []
for frac in np.arange(endloop, startloop+steploop, steploop, dtype="object"):
    print('end', frac)
    calcd = calc(frac)
    all_array.append([frac, Fraction(int(calcd.get_num()), int(calcd.get_den()))])
initial_y = [[enum, i[1]] for enum, i in enumerate(all_array)]
print(all_array.__len__())
# sys.exit() 
#   sys.exit()
# init_y = [calc(i) for i in np.arange(0, start+1, 0.2)]
# plt.figure()
# plt.plot([i[0] for i in all_array], initial_y, label='mad')
print(len(all_array), 'len')
# print(all_array)
# print(all_array.__len__())

def polywer(x): # start is the greater than end
    return [Fraction(x**i) for i in np.arange(end, start+step, step, dtype="object")][::-1]

arr_x = None
def poly_all(arr):
    global arr_x;
    arr_x = np.array([polywer(i[0]) for i in arr], dtype='float64')
    arr_y = np.array([[i[1]] for i in arr], dtype='float64')
    x = np.array([polywer(i[0]) for i in arr], dtype='object')
    # print(len(arr_x), len(arr_y))
    # print(arr_x[0].__len__(), arr_y[0].__len__())
    # np.linalg.solve(arr_x, arr_y)
    # sys.exit()
    y = np.array([[i[1]] for i in arr])
    # print(y)
    fd = time.time()
    matrixx = Matrix(x)
    matrixy = Matrix(y)
    print('linsolving')
    # print(linsolve((matrixx, matrixy)))
    print(f'linsolve took {time.time()-fd} seconds')
    ds = time.time()
    f = graphene.Fraction
    x = np.ndarray.tolist(x)
    prepare_lists(x, y)
    grap = [[f(str(i.numerator), str(i.denominator)) for i in sub_lst] for sub_lst in x]
    # grap = [[f'Fraction({i.numerator}, {i.denominator})' for i in sub_lst] for sub_lst in x]    
    # print(grap)
    # print([[eval(str(i)) for i in sub_lst] for sub_lst in x])
    print(f'A {len(grap)} by {len(grap[0])} matrix')
    ay = time.time()
    graph = graphene.GaussianElimination(grap)
    print(f'graphene took {time.time()-ay} sec')
    print(graph)
    print([eval(str(i)) for i in graph])
    # print(f'custom shit took {time.time()-ds}')
    
    # print(matrixx)
    # print(matrixy)
    # print(mpmath.qr_solve(x, np.ndarray.tolist(arr_y)))
    # print(matrixx**-1 * arr_y)
    # arr_x = np.array([polywer(i[0]) for i in arr], dtype='object')
    print('Matrix')
    # print(x)
    # print(arr_x, 'arr', arr_x[6], arr[6][0]==6, polywer(arr[6][0]), polywer(6))
    # inv = np.linalg.inv(arr_x,)
    # x = np.ndarray.tolist(arr_x)
    # inv = getMatrixInverse(x)
    # inv = np.array(inv)
    # print('why')
    # print(inv)
    # x = np.dot(inv, arr_x)
    # print(np.ndarray.tolist(x))
    # print(inv)
    # return np.dot(inv, arr_y,)
    return np.linalg.solve(arr_x, arr_y)

def readable(arr):
    print('A')

def get_function(arr, x):
    # x = preemptZero(x)
    power_list = list(np.arange(end, start+step, step))
    count = 0
    for i in arr:
        count +=  i*x**power_list.pop()
    # printa(len(power_list), 'na d thing')
    return count

def abacus(x):
    lst = [2.08068745e-02, -7.84285307e-02, -6.78604187e-02, 1.26770834e-01, -1.82963752e+03, 7.31722515e+04, -1.15173266e+06,  9.13788534e+06, -3.89440418e+07, 8.86267389e+07, -9.90133333e+07, 4.12731459e+07, 8.00000000e+00][::-1]
    return 

pw = poly_all(all_array)
sys.exit()
print(pw)
print('power')
# print(pw)
cv = 0
for enum, i in enumerate(arr_x):
    if enum == 6:
        # print(i, 'hi')
        for var, j in enumerate(i):
            val = j*pw[var][0]
            cv += val
        # print(cv, 'hans', enum)
        # print(np.dot(i, pw), 'hans', enum)
# print()
for enum, i in enumerate(arr_x):
        # print(np.dot(i, pw), 'hans', enum)
        pass

for enum, i in enumerate(all_array):
        pass
        # print('mf', i[0], get_function(pw, i[0]), 'model', initial_y[enum][::-1])
print('=====')
print()
# print()
# print(init_y, start, end)
# last_y = itertools.chain.from_iterable([np.ndarray.tolist(get_function(pw, i)) for i in np.arange(0, start+1, 0.2)])
# print(list(last_y))
# print('===last===')
# print([[i, *np.ndarray.tolist(j)] for i, j in zip(list(np.arange(end,start+step, step, dtype="object"))[::-1], pw) if np.ndarray.tolist(j)[0] != 0])
# print()
print(list(filter(lambda _: _[1] > 10e-5, [[i, *np.ndarray.tolist(j)] for i, j in zip(list(np.arange(end,start+step, step, dtype="object"))[::-1], pw) if np.ndarray.tolist(j)[0] != 0])))
xxx = [i[0] for i in all_array]
# xxx.remove(0)
yyy = [get_function(pw, i) for i in xxx]
# plt.figure()
plt.plot(xxx,  yyy)

