import cv2, os, sys
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
from decimal import Decimal
from PIL import Image
# from untitled8 import calc
def calc(x):
    y = x**2
    # y = 9.1*x-1
    # y = 9.1*x**4 + 2.15*x**3 + 7.1*x**2 + 7*x - 4 # 2542.png
    return y

def process_coord(coord): # for PIL image processing
     # new_tup = (coord[0]-1, coord[3]-1, coord[2]+1, coord[1]+1)
     # new_tup = (coord[0], coord[3], coord[2], coord[1])
     new_tup = (coord[0]-1, coord[1]-1, coord[2]+1, coord[3]+5)
     return new_tup

crop = False or 1

if __name__ == '__main__':
    # x = [i for i in np.arange(Fraction(50), step=Fraction(0.5))]
    # y = [calc(i) for i in x]
    # fig = plt.figure(figsize=(15, 10))
    # plt.plot(x, y)
    # plt.grid()
    # # print(list(map(lambda _: float(max(_)), [x, y])))
    # print(list(map(lambda _: str(Decimal(float(max(_)))), [x, y])))
    file = r'2542-1.png'
    # plt.savefig(file)

    if crop:    
        image = cv2.imread(file)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([100, 150, 150], dtype="float64")
        upper_blue = np.array([255, 255, 255], dtype="float64")
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(image, image, mask=mask)
        
        x = image
        tit = []
        try:
            for j in range(len(x)):
                for i in range(len(x[0])):
                    if res[j][i][0] > 10:
                        tit.append((i, j))
        except:
            raise
        crop_coord = (min(tit, key=lambda _: _[0])[0], min(tit, key=lambda _: _[1])[1], max(tit, key=lambda _: _[0])[0], max(tit, key=lambda _: _[1])[1])
        print(crop_coord)
        juju = Image.open(file)
        jujucrop = juju.crop(process_coord(crop_coord))
        # jujucrop = juju.crop((173, 114, 933, 605))
        jujucrop.show()
        # jujucrop.save(file)