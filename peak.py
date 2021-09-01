from scipy.signal import find_peaks as fp
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
# x = electrocardiogram()[20:100]
# print(x)
x = np.array([1, 2, 3, 4, 5, 1, 2, 0, 2])
peaks, _ = find_peaks(x, height=0)
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()