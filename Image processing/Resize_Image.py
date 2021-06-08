#program to resize the image

import cv2
img = cv2.imread("image.png")
 #resize the image using row and column values
newImage = cv2.resize(img, (550, 350))
#display the image
cv2.imshow('Resized Image', newImage)
cv2.waitKey(0)
