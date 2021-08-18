# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:24:25 2021

@author: CHAINZ
"""

import random
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

def funct(x):
    return(x**2 + 4*x**1 - 3*x**3)


# def numpyregression():
#     X=[i for i in np.arange(0,2,0.1)]
#     Y=[random.randint(0,300) for j in X]
#     mymodel= np.poly1d(np.polyfit(X,Y,3))
#     myline = np.linspace(2,95,100)
#     plt.scatter(X,Y, s=2, c="r")
#     plt.plot(myline, mymodel(myline))
#     plt.show()
class poly():
    def __init__(self, x,y,max_power, step):
        self.x= x
        self.y=y
        self.power= max_power
        self.step=step
    def multipolyregression(self):
        X=[[i**j  for j in np.arange(1,self.power, self.step)]for i in self.x]
        regr=linear_model.LinearRegression()
        regr.fit(X,self.y)
        print(regr.coef_)
        return(regr.coef_)

# def sklearnregression():
#     X1=[i for i in np.arange(0,14,1)]
#     X2=[i**2 for i in X1]
#     X3=[i**3 for i in X1]
#     X=[[i,j,k] for i,j,k in zip(X1,X2,X3)]
#     Y=[funct(j) for j in X1]
#     regr=linear_model.LinearRegression()
#     regr.fit(X,Y)
#     print(regr.coef_)
#     return(regr.coef_)


# sklearnregression()
X=[i for i in np.arange(0,14,1)]
Y=[funct(j) for j in X]
reg=poly(X,Y,4,1)
coeficients=reg.multipolyregression()
