import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
def calc(x):
    # y = 9.1*x-1
    # y = x**2
    y = 5*x**4 + 2.15*x**3 + 7.1*x**2 + 7*x + 40 # 2542.png
    # y = 5*x**4
    # y = 2.15*x**3 + 7.1*x**2 + 7*x - 4 # 2542.png
    # y = x + 5
    return y

def process_coord(coord): # for PIL image processing
     new_tup = (coord[0]-1, coord[3]-1, coord[2]+1, coord[1]+1)
     return new_tup

if __name__ == '__main__':
    x = [i for i in np.arange(Fraction(-5), Fraction(5), step=Fraction(0.00001))]
    y = [calc(i) for i in x]
    fig = plt.figure(figsize=(40, 40))
    ax = fig.add_subplot(111)
    
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position('zero')
    #ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)    
    plt.plot(x, y)
    # px = plt.xticks()
    # xlwz = px[0].tolist()
    # xlwz.remove(0) # list without zero
    # plt.xticks(xlwz)
    
    # py = plt.yticks()
    # ylwz = py[0].tolist()
    # ylwz.remove(0) # list without zero
    # plt.yticks(ylwz)
    # plt.grid()
    file = r'2540.png'
    plt.savefig(file)