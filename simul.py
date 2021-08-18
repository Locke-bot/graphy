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
import functools
import string, sys


def gaussian(arr, start, end, step):

    def polywer(x): # start is the greater than end
        return [Fraction(x**i) for i in np.arange(end, start, step, dtype="object")][::-1]

    def solve(arr):
        arr_x = np.array([polywer(i[0]) for i in arr], dtype='float64')
        arr_y = np.array([[i[1]] for i in arr], dtype='float64')
        x = np.array([polywer(i[0]) for i in arr], dtype='object') + Fraction()
        y = np.array([[i[1]] for i in arr])
        # print(y)
        fd = time.time()
        matrixy = Matrix(y)
        ds = time.time()
        f = graphene.Fraction
        x = np.ndarray.tolist(x)
        prepare_lists(x, y)
        grap = [[f(str(i.numerator), str(i.denominator)) for i in sub_lst] for sub_lst in x]
        graph = graphene.GaussianElimination(grap)
        return np.linalg.solve(arr_x, arr_y), graph
    
    return solve(arr)