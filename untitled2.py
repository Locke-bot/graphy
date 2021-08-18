import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

# n = 10
# constant = 15
# step = Fraction(1, 100)
# def calc_y(x):
#     try:
#         y = 1/x + constant
#     except ZeroDivisionError:
#         y = float('inf')
#     return y

# x = [i for i in np.arange(-n, n, step)]
x = [i for i in np.arange(0, 30, Fraction(1, 10))]
# y = [calc_y(i) for i in x]
y = [i**2 for i in x]
# print(calc_y(1))
fig = plt.figure(figsize=(12, 8))
#fig(figsize=(20, 15))
ax = fig.add_subplot(111)

#ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
#ax.spines['top'].set_color('none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.grid()
plt.plot(x, y)
# plt.savefig('x_square.png')
plt.show()