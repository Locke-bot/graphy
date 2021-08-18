# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:21:58 2021

@author: CHAINZ
"""
import time
from graphOCR_2 import Graph
import cv2
from matplotlib import pyplot as plt



gridunit=20

inittime= time.time()       

img= cv2.imread("x_square.png", cv2.IMREAD_GRAYSCALE) 

x= Graph(img,gridunit)

cor=x.get_coordinates()

plt.plot(cor[0], cor[1])
plt.grid(True)
plt.show()

print([[cor[0][i], cor[1][i]] for i in range(len(cor[1]))])

print(time.time()-inittime)
