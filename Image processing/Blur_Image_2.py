#program to blur image using median blur
import cv2
img = cv2.imread("image.png")
#blur image using median blur
blur_image = cv2.medianBlur(img, 5)
#show the image
cv2.imshow('Original Image', img)
cv2.imshow('Blur Image', blur_image)
cv2.waitKey(0)
