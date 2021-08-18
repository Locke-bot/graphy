# -*- coding: utf-8 -*-
"""
Created on Fri May  7 06:57:00 2021

@author: Unrated
"""

import matplotlib.pyplot as plt
import cv2, numpy as np
from graphene import GaussianElimination, Fraction
import os, sys, fractions
import copy

file = r'2540.png'
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
res2 = copy.deepcopy(res)
# cv2.imshow('moddded out', hsv)
cv2.imshow('mask off', mask)
cv2.imshow('res', res)

# def Fraction(a, b=None):
#     if b is None:
#         return a
#     return a/b

x = image
height = len(x)
length = len(x[0])
# height = Fraction(len(x))
# length = Fraction(len(x[0]))
# graph_height = Fraction(938536, 1000)
# graph_width = Fraction(31395, 1000)
graph_height = 938.536
graph_width = 31.395
coords = [[], []]
xappend = coords[0].append
yappend = coords[1].append
print(graph_width/length)
try:
    for j in range(len(x)):
        for i in range(len(x[0])):
            # if all(res2[j][i] != [0, 0, 0]):
            if res2[j][i][0] > 10:
                x[j][i] = [255, 255, 0]
                xx = i*graph_width/length
                yy = graph_height*(height-j)/height
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
cv2.imshow('original', image)
cv2.imshow('peeves', res2)
img = res2
# img = cv2.imread('lena.jpg', 1)
def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 255, 255), 2)
        # cv2.imshow('image', img)
  
    # checking for right mouse clicks     
    if event==cv2.EVENT_RBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        # cv2.imshow('image', img)
  
# driver functionzy
cv2.setMouseCallback('peeves', click_event)
plt.grid()
diff = []
# for i in range(len(coords[0])):
#     x = coords[0][i]
#     y = coords[1][i]
#     # print(x, y, x**2, f'off by {((x**2-y)/x**2)*100} %')
#     print(x, y, x**2, f'different by {x**2-y}')
#     diff.append(x**2-y)
zipped_coord = list(zip(coords[0], coords[1]))
n = 5 # 375/n
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
x_list, y_list = [fractions.Fraction(i) for i in coords[0]], [fractions.Fraction(i) for i in coords[1]]
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
        # print(mat[i][j], str(mat[i][j]))
        mat[i][j] = Fraction(str(mat[i][j]))
ans = GaussianElimination(mat)
print([eval(str(i)) for i in ans][::-1])
