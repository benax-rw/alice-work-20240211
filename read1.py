from PIL import Image
import pytesseract
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

col = Image.open("./picture.png")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("gray_scale.png")


image = cv2.imread('gray_scale.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

thresh = cv2.GaussianBlur(thresh, (3,3), 0)
img1 = np.array(thresh)
data = pytesseract.image_to_string(img1, config='--psm 11 digits')
print(data)

cv2.imshow('thresh', thresh)
cv2.waitKey()