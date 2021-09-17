# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 23:56:45 2021

@author: Unrated
"""

import cv2, sys, random
import pytesseract
import assline
from PIL import Image
import numpy as np
from decimal import Decimal
from graphene import GaussianElimination, Fraction

# constants, dbtx, dbty, poly_deg, scalex, scaley

dbtx = 152 # distance between ticks in pixel, x axis.
dbty = 69 # distance between ticks in pixel, y axis.
poly_deg = 30
print(f"deg={poly_deg}")

file = '2540.png'

img = cv2.imread(file)

safari = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
flag, thresh = cv2.threshold(safari, 0, 255, 16)
edges = cv2.Canny(thresh, 50, 190)
minLineLength = 100
maxLineGap = 100
lino = []
lines = cv2.HoughLines(edges, 1, np.pi/360, 200).tolist() # top
mxsd = 60 # max x scale distance in pixel, as in maximu distance of scale lettering from the x axis
mysd = 60 # max y scale distance in pixel

def conv_ang(ang, mode):
    if mode == 'rad': return ang*180/np.pi
    if mode == 'deg': return ang*np.pi/180
    
# sys.exit()
    
def bound_int(n, maxi, mini=0):
    assert mini <= maxi, "mini greater than maxi"
    return max(mini, min(n, maxi)) # bounding n

length, height = img.shape[:2][::-1]
coords = []
for enum, line in enumerate(lines):
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        u = 1000
        x1 = int(x0 + u*(-b))
        x1 = bound_int(x1, length)
        
        y1 = int(y0 + u*(a))
        y1 = bound_int(y1, height)
        
        x2 = int(x0 - u*(-b))
        x2 = bound_int(x2, length)
    
        y2 = int(y0 - u*(a))
        y2 = bound_int(y2, height)
        coords.append([x1, y1, x2, y2])
        # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # cv2.line(img,(x1,y1),(x2,y2), tuple(random.randint(0, 255) for i in range(3)), 2)
    # cv2.imshow(f"line-{enum}", img)
    # break
    enum += 1
# sys.exit()
al = 2 # alowed variation for supposedly vertical and horizontal lines.
left, bottom = None, None

def check_orientation(coords):
    if abs(coords[0] - coords[2]) < al:
        return 0 # vertical
    if abs(coords[1] - coords[3]) < al:
        return 1 # horizontal
    return 2 # slant or otherwise

for enum, line in enumerate(coords, start=1):
    # line = line[0]
    orit = check_orientation(line)
    if not orit: # vertical
        if not left: left = line
        elif (line[0] < left[0]):
            left = line
    elif orit == 1:
        if not bottom: bottom = line
        elif (line[1] > bottom[1]):
            bottom = line
            
def process_coord(coord, inclusive=True): # for PIL image processing
    new_tup = (coord[0]-inclusive, coord[3]-inclusive, coord[2]+inclusive, coord[1]+inclusive)
    return new_tup

def process_scales(et, axis): # extracted scale, this would have to be sophisticated
    # some gradations might be skipped, currently taking the smallest, sometimes signs are missed too
    splt = [i.rstrip('-') for i in et.split() if i]
    if  len(splt) == 1:
        raise ValueError
    else:
        if axis == "x":
            diffs = []
            for i in range(1, len(splt)):
                try:
                    diff = int(splt[i]) - int(splt[i-1])
                    diffs.append(diff)                        
                except ValueError:
                    pass
            return min(diffs)
            # return min([-j for j in [splt[i-1]-splt[i] for i in  range(1, len(splt))]])
        elif axis == "y":
            diffs = []
            for i in range(1, len(splt)):
                try:
                    diff = int(splt[i-1]) - int(splt[i])
                    diffs.append(diff)                        
                except ValueError:
                    pass
            return min(diffs)
            # return min([splt[i-1]-splt[i] for i in  range(1, len(splt))])

def prepare_image(img):
    return cv2.resize(img, None, fx=2, fy=2)

enum = 1
for x1, y1, x2, y2 in (bottom, left):
    image = np.array(safari)
    # cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    new = np.full_like(image, 255)
    if enum == 1:
        miny = max(y1, y2) # most times y1 and y2 will be equal, just providing for a skewy situation
        rows = np.array([i for i in range(miny, miny+mysd+1)], dtype=np.intp)
        # rows = np.array([i for i in range(image.shape[0])], dtype=np.intp)
        column = np.array([i for i in range(image.shape[1])], dtype=np.intp)
        # column = np.array([i for i in range(eff_x-mxsd, eff_x+1)])
        new[rows[:, np.newaxis], column] = image[rows[:, np.newaxis], column]
        new = prepare_image(new)
        # cv2.imshow(f"just us x", new)
        # print(f'x-scale = {pytesseract.image_to_string(new, config="--psm 6 digits tessedit_char_whitelist=-+0123456789").strip()}')
        scalex = abs(process_scales(pytesseract.image_to_string(new, config="--psm 6 digits tessedit_char_whitelist=-+.0123456789").strip(), "x"))
        print(f'x-scale = {scalex}')
        
    elif enum == 2:
        rows = np.array([i for i in range(image.shape[0])], dtype=np.intp)
        minx = min(x1, x2)
        column = np.array([i for i in range(minx-mxsd, minx+1)]) # so a distance of mxsd from the most rightward one
        new[rows[:, np.newaxis], column] = image[rows[:, np.newaxis], column]
        edgy = cv2.Canny(new, 50, 190)
        new = prepare_image(new)
        # cv2.imshow(f"just us y", new)
        # print(pytesseract.image_to_string(new, config="--psm 4 digits tessedit_char_whitelist=-+.0123456789").strip())
        scaley = abs(process_scales(pytesseract.image_to_string(new, config="--psm 4 digits tessedit_char_whitelist=-+.0123456789").strip(), "y"))
        # the difference between ticks should always be +ve I think
        print(f'y-scale = {scaley}')
        # print(f'y-scale = {pytesseract.image_to_string(new, config="--psm 4 digits tessedit_char_whitelist=-+0123456789").strip()}')
    enum += 1

# cv2.waitKey()
# cv2.destroyAllWindows()
# sys.exit()
# scaley = scaley*10**6
# scalex = 2
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100, 150, 150], dtype="float64")
upper_blue = np.array([255, 255, 255], dtype="float64")
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
res = cv2.bitwise_and(img, img, mask=mask)

x = img
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
maxx = scalex*(crop_coord[2] - left[0])/dbtx
maxy = scaley*(bottom[1] - crop_coord[1])/dbty
print(maxx, maxy, 'maxi')

coords = [[], []]
xappend = coords[0].append
yappend = coords[1].append

count = 0
for j in range(len(x)):
    for i in range(len(x[0])):
        if res[j][i][0] > 10:
            xx, yy = scalex*(i - left[0])/dbtx, scaley*(bottom[1] - j)/dbty
            xappend(xx)
            yappend(yy)

# ======
            
x_list, y_list = coords[0], coords[1]

assert len(x_list) == len(y_list)

power_list = [None]*(1+2*poly_deg)

def power(deg, start=1, end=len(x_list)): # 1 indexed, start and end inclusive
    power_list[deg] = power_list[deg] or sum([i**deg for i in x_list[start-1:end]])
    return power_list[deg]
    
mat = []

def reg(): # this gives a poly_deg+1 square matrix
    asc_num = [i for i in range(1+2*poly_deg)]
    for i in range(len(asc_num)-poly_deg):
        mat.append(list(map(power, asc_num[i:i+poly_deg+1])) + [sum([y_list[j]*x_list[j]**i for j in range(len(x_list))])])
    return mat
reg()
for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] = Fraction(str(Decimal(mat[i][j]))) # decimal to remove the e from floats
ans = GaussianElimination(mat)
coeffs = [eval(str(i)) for i in ans][::-1]
print(coeffs)

# for testing only, variables not accessible in production

def catf(): #conv_ans_to_func
    ps = "" # power string
    length = len(coeffs)
    for i in range(len(coeffs)):
        coeff = coeffs[i]
        ps += f"{coeff}*x**{length-i-1} + "
    ps = ps.rstrip("+ ")
    exec("y = ps")
    # x = 
    return eval('y')

rss = 0
func = catf()
def calc_rss(): # calculate the residual sum of squares
    global rss
    for i in range(len(x_list)):
        x = (x_list[i])
        rss += ((y_list[i] - eval(func))**2)
    return rss
print()
print(calc_rss())
cv2.waitKey(0)
cv2.destroyAllWindows()