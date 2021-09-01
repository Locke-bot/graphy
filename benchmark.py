from graphene import *
import gaussianpy as gp
import cygaussianpro as cgp
import cygaussian as cg
import numpy as np
import fractions
import time, sys, copy
def prepare_lists(x_array, y_array):
    for i in range(len(y_array)): # augmenting
        x_array[i].append(*y_array[i])

def fract(x_array):
    for i in range(len(x_array)):
        for j in range(len(x_array[i])):
            x_array[i][j] = Fraction(str(x_array[i][j]))
       
def py_fract(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = fractions.Fraction(str(x[i][j]))
    return x

def py(thelist, convert=True):
    for i in range(len(thelist)):
        for j in range(len(thelist[0])):
            thelist[i][j] = fractions.Fraction(thelist[i][j]) 
    if not convert:
        return thelist
    return np.array(thelist)

if __name__ == '__main__':
    n = 120
    # this creates a n by n matrix, with the lowest and highest points as -500 and 500 respectively
    x_array = np.random.uniform(-500, 500, [n, n])
    y_array = [[np.random.randint(-5000, 5000)] for i in range(n)]
    # x_array = [[1, 2, 3],
    #            [4, 0, 1],
    #            [3, 2, 3]]
    # y_array = [[10], [8], [12]]
    # print(y_array)
    # y_array = []
    x_array = np.ndarray.tolist(x_array)
    
    print('numpy starting')
    a = time.time()
    solve = np.linalg.solve(x_array, y_array)
    print(f'numpy took {time.time()-a} seconds for a {n} by {n} matrix')
    # print(solve)
    prepare_lists(x_array, y_array)
    
    b = time.time()
    fc = gp.GaussianElimination(py(copy.deepcopy(x_array)))
    print(f'python version took {time.time()-b} seconds for a {n} by {n} matrix')
    # print(fc)
    
    e = time.time()
    st = cg.GaussianElimination(py(copy.deepcopy(x_array), False))
    print(f'cg version took {time.time()-e} seconds for a {n} by {n} matrix')
    print(fc==st)
    
    d = time.time()
    rt = cgp.GaussianElimination(py(copy.deepcopy(x_array)))
    print(f'cgp version took {time.time()-d} seconds for a {n} by {n} matrix')
    print(fc==rt)
    # print([float(i) for i in rt])
    
    fract(x_array)
    print('Gauss starting')
    c = time.time()
    gaus = GaussianElimination(x_array)
    print(f'gauss took {time.time()-c} seconds for a {n} by {n} matrix')
    # print(gaus)
    # print([eval(str(i)) for i in gaus])