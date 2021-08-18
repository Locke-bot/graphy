# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:21:58 2021

@author: CHAINZ
"""
import time
from graphOCR_ import Graph, Graph2
import cv2
from matplotlib import pyplot as plt



gridunit=6

inittime= time.time()       

img= cv2.imread("x_square.png", cv2.IMREAD_GRAYSCALE) 


#for specified axis where [0,100] means minimum x is 0 and maximum x is 100...likewise [0.0,1.0] for y
x= Graph2(img,gridunit, [0, 50], [0, 2500])

cor=x.get_coordinates()

plt.plot(cor[0], cor[1])
plt.grid(True)
plt.show()
print([[cor[0][i], cor[1][i]] for i in range(len(cor[1]))])


# for unspecified_axis
x= Graph(img,gridunit)

cor=x.get_coordinates()

plt.plot(cor[0], cor[1])
plt.grid(True)
plt.show()
print([[cor[0][i], cor[1][i]] for i in range(len(cor[1]))])


print(time.time()-inittime)
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
