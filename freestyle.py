import cv2
import numpy as np
file = '2540.png'
# dbtx = 406 # distance between ticks in pixel, x axis.
# dbtx = 204 # distance between ticks in pixel, x axis.
# dbtx = 102 # distance between ticks in pixel, x axis.
# dbty = 104 # distance between ticks in pixel, y axis.
# dbty = 139 # distance between ticks in pixel, y axis.
# dbty = 273 # distance between ticks in pixel, y axis.
poly_deg = 4
print(f"deg={poly_deg}")

img = cv2.imread(file)
safari = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
flag, thresh = cv2.threshold(safari, 0, 255, 16)
edges = cv2.Canny(thresh, 50, 190)
# minLineLength = 100
# maxLineGap = 10
# cv2.imshow('thresh', thresh)
cv2.imshow('edge', edges)
# lines = cv2.HoughLinesP(edges, 1, np.pi/360, 20, minLineLength, maxLineGap).tolist() # top



# for line in lines:
    # x1, y1, x2, y2 = line[0]
    # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

lines = cv2.HoughLines(edges, 1, np.pi/360, 30).tolist() # top

def bound_int(n, maxi, mini=0):
    assert mini <= maxi, "mini greater than maxi"
    return max(mini, min(n, maxi)) # bounding n

length, height = img.shape[:2][::-1]

for enum, line in enumerate(lines):
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        u = 100
        x1 = int(x0 + u*(-b))
        x1 = bound_int(x1, length)
        
        y1 = int(y0 + u*(a))
        y1 = bound_int(y1, height)
        
        x2 = int(x0 - u*(-b))
        x2 = bound_int(x2, length)
    
        y2 = int(y0 - u*(a))
        y2 = bound_int(y2, height)
        # coords.append([x1, y1, x2, y2])
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        # cv2.line(img,(x1,y1),(x2,y2), tuple(random.randint(0, 255) for i in range(3)), 2)
# cv2.imshow(f"line-{enum}", img)
cv2.imshow("frustrated", img)
cv2.waitKey()
cv2.destroyAllWindows()