import example
import random
import time, sys
import numpy as np
gcd = example.gcd
# Benchmarking.
def py_gcd(x, y):
    g = y
    while (x > 0):
        g = x
        x  = y%x
        y = g
    return g


print(py_gcd(5, 15))
Range = 1000

xx = [random.randint(0, 10000) for i in range(Range)]
yy = [random.randint(0, 10000) for i in range(Range)]
xx = [np.random.randint(100, 1000000) for i in np.arange(0, Range, dtype='uint32') ]
print('just')
yy = [np.random.randint(100, 1000000) for i in np.arange(0, Range, dtype='uint32') ]
print('starting')
start_py = time.time()
for i in range(len(xx)):
    py_gcd(xx[i], yy[i])
print(f'python took {time.time()-start_py}')
start_c = time.time()
for i in range(len(xx)):
    gcd(xx[i], yy[i])
print(f'C took {time.time()-start_c}')