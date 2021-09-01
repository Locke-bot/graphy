from PIL import Image
import pytesseract
import cv2
import numpy as np

file = r'x_scale.png'
img = cv2.imread(file)
# image = np.array(img)
# kernel = np.ones((1, 1), np.uint8)
# img = cv2.dilate(img, kernel, iterations=100)
# img = cv2.erode(img, kernel, iterations=1)
image = cv2.resize(img, None, fx=2, fy=2)
# image = cv2.GaussianBlur(img, (5, 5), 0)

# cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# string = pytesseract.image_to_string(img, config="--psm 6 digits tessedit_char_whitelist=0123456789").strip()
string = pytesseract.image_to_string(image, config="--psm 6").strip()
print(string)
# cv2.imshow('image', image)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
