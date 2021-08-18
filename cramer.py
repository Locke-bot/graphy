# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:45:56 2021

@author: Unrated
"""

import string
from fractions import Fraction
import math, sys
from sympy import *
from itertools import combinations, permutations
import local_array as lca

init_printing()
def split_float(flt, fraction=False):
    flt_string = str(flt)
    index = flt_string.find('.')
    if index == -1: # has no decimal point
        if fraction:
            return Fraction(int(flt))
        return flt
    if fraction:
        return Fraction(int(flt_string[:index] + flt_string[index+1:]), 10**(len(flt_string)-index-1))
    return int(flt_string[:index] + flt_string[index+1:]), 10**(len(flt_string)-index-1)

def generate_var(n):
    # there are 26 letters
    # if the no of desired variables is more than 26
    # then it becomes aa, ab, ac ...
    # n = 26 ^ x
    x = math.ceil(math.log(n)/math.log(26))
    letters = string.ascii_lowercase
    
    def recur(i, c=''):
        # print(i)
        i, mod = divmod(i, 26)
        c = letters[mod]+c
        # print(i, mod, c)
        if i == 0:
            return c
        if i <= 25:
            c = letters[i] + c
            return c
        return recur(i, c)
    count = 0
    for i in range(n):
        res = ("{0:a>" + f"{x}" + "}").format(recur(i+count))
        try:
            exec(f'{res} = 1')
            yield res
        except SyntaxError:
            # due to assignment to keywords
            count += 1
            res = ("{0:a>" + f"{x}" + "}").format(recur(i+count))
            yield res

# This is of the form ... + cx^3 + bx^2 + ax = 0
class MismatchedError(ValueError):
    pass

def matrix_to_list(mat):
    lst, a = [], 0
    row, col = mat.shape
    for i in range(row):
        b = a+col
        lst.append(mat[a:b])
        a = b
    return lst

mtl = matrix_to_list
    
def cramer(mat, coeff): 
    # cramer for augmented matrix i.e a n+1 by n matrix, with coeff zero indexed
    den = Matrix([i[:-1] for i in mtl(mat)]).det()
    copy = mat.copy()
    copy.col_del(coeff)
    num = copy.det()
    return num/den

def generate_matrix(pairs):
    global res_symbols, coeff_symbols
    matrix_list = []
    for i in range(len(pairs)):
        row = [Symbol(f"x{i+1}")**j for j in range(lowest, highest, step)]
        matrix_list.append(row)
        coeff_symbols.append(Symbol(f"x{i+1}"))
    ys = [Symbol(f'y{i}') for i in range(1, len(pairs)+1)]        
    matrix_list = Matrix(matrix_list)
    matrix_list = matrix_list.col_insert(len(matrix_list), Matrix(ys))
    return matrix_list

def juggler(mat, index=0): # the whole goddamn matrix
    if index:
        mat = mat.row_insert(0, mat.row(index))
        mat.row_del(index+1) # the rows has increased by 1, as per line above.
    the_cram = []
    row, col = mat.shape
    for i in range(row-order+1):
        if i == 0:
            mat_lst = mtl(mat)
        else:
            mat_lst = mtl(mat)
            del mat_lst[1]
        mat = Matrix(mat_lst)
        eff_mat = Matrix(mat_lst[:order])
        the_cram.append(cramer(eff_mat, 0))
        # the_cram.append(cramer(eff_mat, index))
    return the_cram, index

def mean(collection, flt=False):
    average = sum(collection)/len(collection)
    if flt:
        return float(average)
    return average

the_equations = {}
    
def jug_eqn(jugg):
    
    def equate(a, b):
        eqn = Eq(a-b, 0)
        soln = solve(eqn, res_symbols[index])[0]
        if index == 0:
            pprint(soln)
        res = soln.subs(dct)
        ress.append(res)
        return res.subs(ay_dict)
    
    jug, index = jugg
    global eqn, soln
    dct = {coeff_symbols[i]:pairs[i] for i in range(len(pairs))}
    results = []
    eqn = the_equations.get(res_symbols[index])
    if eqn:
        return [res.subs(ay_dict) for res in eqn]
    else:
        ress = [] # to add to the dict
        for i in range(len(jug)-1):
            a, b = i, i+1
        # for i in combinations(range(len(jug)), 2):
        #     a, b = i
            results.append(equate(jug[a], jug[b]))
        the_equations[res_symbols[index]] = ress
        return results
# def multiple(pairs, order):
#     cl = order + 1
#     matrix = generate_matrix(matrix[:cl])
#     jug1 = juggler()

array = lca.array[:100]
# pairs = [i[0] for i in array]
pairs = [1, 7, 9, 10, 3]
# 3x**2 + 2x
res_symbols = [] # the y1, y2, ...
coeff_symbols = []
order, step, lowest = 2, 1, 1
highest = lowest + (order*step)
for i in range(len(pairs)): # to make the result symbol available
    exec(f"y{str(i+1)}=Symbol('y{str(i+1)}')")
    y = eval(f"y{str(i+1)}")
    res_symbols.append(y)
    
for i in range(len(pairs)): # to make the coeff symbol available
    exec(f"x{str(i+1)}=Symbol('x{str(i+1)}')")

if len(pairs) < (order + 1):
    raise MismatchedError
    
for i in res_symbols: # to make the result symbol asvailable
    exec(f"{str(i)}=i")
    
for i in coeff_symbols: # to make the coeff symbol available
    exec(f"{str(i)}=i")
    
# apprx_y = [i[1] for i in array]
apprx_y = [4.9, 162, 261.2, 321, 34.1] # approximated ys
correct_value = [5, 161, 261, 320, 33]
ay_dict = {Symbol(f'y{i+1}'):apprx_y[i] for i in range(len(apprx_y))}
matrix = generate_matrix(pairs)
eqn, soln = None, None
for i in range(1):
    hold = []
    for j in range(len(pairs)):
        jug1 = juggler(matrix, index=j)
        hans = jug_eqn(jug1)
        # pprint(hans)
        avg = mean(hans, flt=True)
        hold.append(avg)
        # pprint(avg)
        ay_dict[res_symbols[j]] = avg
    # print(ay_dict)
print()
for h in hold:
    pprint(h)
# xy = [[pairs[i], hold[i]] for i in range(len(pairs))]
# print([[split_float(i[0], fraction=True), split_float(i[1], fraction=True)] for i in xy])
# import copy
# prs = copy.deepcopy(pairs)
# multiple(pairs, order)
# print(prs)