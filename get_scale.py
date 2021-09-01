import cv2, copy
import pytesseract
from PIL import Image
import numpy as np
file = '2542-1.png'
img = cv2.imread(file)
safari = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
flag, thresh = cv2.threshold(safari, 0, 255, cv2.THRESH_OTSU)
# element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# thresh = cv2.erode(thresh, element)
edges = cv2.Canny(thresh, 50, 190)
minLineLength = 100
maxLineGap = 200
lino = []
# cv2.imshow("origin", safari)
# cv2.imshow("thresh", thresh)
# cv2.imshow("edge", edges)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 275, minLineLength, maxLineGap).tolist() # top
left, bottom = None, None
def check_orientation(coords):
    if coords[0] == coords[2]:
        return 0 # vertical
    if coords[1] == coords[3]:
        return 1 # horizontal
    return 2 # slant or otherwise

for enum, line in enumerate(lines, start=1):
    line = line[0]
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

def process_scales(et, axis): # extracted  text
    splt = [int(i.rstrip('-')) for i in et.split('\n') if i]
    if  len(splt) == 1:
        raise ValueError
    else:
        if axis == "x":
            return min([-j for j in [splt[i-1]-splt[i] for i in  range(1, len(splt))]])
        elif axis == "y":
            return min([splt[i-1]-splt[i] for i in  range(1, len(splt))])
            

enum = 1
print(left, bottom)
for x1, y1, x2, y2 in (left, bottom):
    img = cv2.imread(file)
    kx = Image.fromarray(img)
    if enum == 1: # left
        kp = kx.crop(process_coord([0, y1, x2, y2], inclusive=False))
        kp = kp.resize((i*3 for i in kp.size))
        kp.show()
        string = pytesseract.image_to_string(kp, config="digits tessedit_char_whitelist=0123456789").strip()
        # print(process_scales(string, "y"))
    elif enum == 2: # bottom
        kp = kx.crop(process_coord([x1, kx.size[1], x2, y2], inclusive=False))
        kp = kp.resize((i*5 for i in kp.size))
        string = pytesseract.image_to_string(kp, config="digits tessedit_char_whitelist=0123456789").strip()
        kp.show()
        # print(process_scales(string, "x"))
    enum += 1
cv2.waitKey()
cv2.destroyAllWindows()