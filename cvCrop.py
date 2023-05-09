import cv2
image = cv2.imread('/Users/gabriel/Downloads/lena_resized.jpg')
y=300
x=300
h=200
w=200
lena_cropped = image[y:y+h, x:x+w]

# Save cropped image
cv2.imwrite("/Users/gabriel/Downloads/lena_cropped.jpg", lena_cropped)

cv2.imshow('Lena Cropped', lena_cropped)
cv2.waitKey(0)
