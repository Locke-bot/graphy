# -*- coding: utf-8 -*-
"""
Created on Fri May  7 06:57:00 2021

@author: Unrated
"""

import matplotlib.pyplot as plt
import cv2, numpy as np
from  decimal import Decimal
from graphene import GaussianElimination, Fraction
import os, sys, fractions
import copy
import remgrid

file = r'2542-1.png'
image = cv2.imread(file)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower_blue = np.array([0, 100, 200])
upper_blue = np.array([100, 225, 225], dtype="float64")
lower_blue = np.array([0, 0, 0], dtype="float64")
lower_blue = np.array([100, 150, 150], dtype="float64")
upper_blue = np.array([255, 255, 255], dtype="float64")
# upper_blue = np.array([255, 255, 255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow('moddded out', hsv)
cv2.imshow('mask off', mask)
cv2.imshow('res', res)

x = image

graph_height = 938.536 # 81 , #154
# graph_width, graph_height = 49.480519480519480519480519480519, 6123.4567901234567901234567901235
# graph_width, graph_height = 49.480519480519480519480519480519, 6123.4567901234567901234567901235
# graph_width, graph_height = 50, 6432.0987654320987654320987654321
# maxx, maxy = 49.5, 449.45
# maxx, maxy = 49.35064935064935, 6122.267418349627
# maxx, maxy = 49.5, 54633604.493749998509883880615234375
# maxx, maxy = 49.5, 449.4499999999999886313162278383
maxx, maxy = 49.54248366013072, 2470.0
coords = [[], []]
xappend = coords[0].append
yappend = coords[1].append
# print(graph_width/length)
count = 0
new = True
tit = []
try:
    for j in range(len(x)):
        for i in range(len(x[0])):
            # if all(res[j][i] != [0, 0, 0]):
            if res[j][i][0] > 10:
                tit.append((i, j))
                x[j][i] = [255, 255, 0]
                if new:
                    # print(xx, yy)
                    new = False
                    xx, yy = maxx, maxy
                    # xappend(maxx)
                    # yappend(maxy)  
                    height = len(x)-j
                    length = i
                    # print(height, length, i, len(x[0]), len(x))
                    # continue
                else:
                    xx = i*maxx/length
                    yy = maxy*(len(x)-j)/height
                # if coords[0].__len__() > 10:
                    # raise ValueError
                if coords[1] and coords[1][-1] == yy: # use the new one instead
                    coords[0].pop()
                    coords[1].pop()
                if coords[0] and coords[0][-1] == xx: # use the old one instead, these are from observations.
                    continue
                # print(i, height-j, xx, yy)
                xappend(xx)
                yappend(yy)
except:
    raise
print(min(tit, key=lambda _: _[0]) + max(tit, key=lambda _: _[0]))
# sys.exit()
cv2.imshow('original', image)
cv2.imshow('peeves', res)
img = res
# img = cv2.imread('lena.jpg', 1)
diff = []
for i in range(len(coords[0])):
    x = coords[0][i]
    y = coords[1][i]
    # print(x, y, x**2, f'off by {((x**2-y)/x**2)*100} %')
    # print(x, y, x**2, f'different by {x**2-y}')
    c = remgrid.calc(x)
    diff.append(abs(100*(c-y)/c))
zipped_coord = list(zip(coords[0], coords[1]))

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
    
# xy = [[split_float(i, fraction=True), split_float(j, fraction=True)] for i, j in zipped_coord[::n]]
# print(xy)
# plt.plot(coords[0], coords[1])

# print([[i, j] for i, j in [coords[0][::5], coords[0][1]]])
# cv2.waitKey(0)
cv2.destroyAllWindows()
# x_list, y_list = [fractions.Fraction(i) for i in coords[0]], [fractions.Fraction(i) for i in coords[1]]
x_list, y_list = coords[0], coords[1]
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
            # mat[i][j] = str(mat[i][j])
            # print(mat[i][j], str(Decimal(mat[i][j]))) # decimal to remove the e from floats
        mat[i][j] = Fraction(str(Decimal(mat[i][j])))
ans = GaussianElimination(mat)
print([eval(str(i)) for i in ans][::-1])