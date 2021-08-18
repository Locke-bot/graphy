import cv2
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def calc_y(x):
    return x**2
    # return 2.4*x**2 + 5*x - 4

x = [i for i in np.arange(Fraction(50), step=Fraction(0.5))]
y = [calc_y(i) for i in x]
fig = plt.figure(figsize=(30, 30))
plt.plot(x, y)
plt.grid()
plt.savefig('2540.png')
# plt.scatter(x, y, s=0.5, color='black', label='Phase C')
# image = cv2.imread('x_square.png')
# image=cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LANCZOS4)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# n = 100
# # ret, threshmod = cv2.threshold(gray_image, n, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# ret, thresh = cv2.threshold(gray_image, n, 255, cv2.THRESH_BINARY_INV)
# ret, threshsv = cv2.threshold(hsv, n, 255, cv2.THRESH_BINARY)
# # edges = cv2.Canny(gray_image, 100, 200)
# # threshx = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
# # cv2.imshow('thresh_inv & otsu', image)
# cv2.imshow('threshv', thresh)
# # cv2.imshow('edge', edges)
# # cv2.imshow('hedge', cv2.Canny(thresh, 100, 200))
# # cv2.imshow('edghe', cv2.Canny(threshmod, 100, 200))
# cv2.imshow('threshsv', threshsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()