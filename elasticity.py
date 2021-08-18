# -*- coding: utf-8 -*-
"""
Created on Thu May  6 00:24:12 2021

@author: Unrated
"""

# program to calculate point and arc elasticity, demand theory.

def arc(p1, p2, q1, q2):
    return ((p1+p2)*(q2-q1))/((q1+q2)*(p2-p1))

def point(p1, p2, q1, q2):
    return ((p1)*(q2-q1))/((q1)*(p2-p1))

price_prev = None
enum_prev = None
price = list(range(100, 0, -10))
# price = list(range(3000, 0, -300))
# print(price)
quantity = [i for i in range(1, 11, 1)]
# quantity = list(range(30, 301, 30))
print(quantity)
for enum, i in zip(quantity, price):
    if price_prev: # if it has history, execute.
        # print(price_prev, i, enum_prev, enum, 'enumi')
        # print(round(arc(price_prev, i, enum_prev, enum), 3))
        print(round(point(price_prev, i, enum_prev, enum), 3))
    enum_prev = enum
    price_prev = i
    