#program to make an image blurry
#Gaussian blur
import cv2
#show the image
img = cv2.imread("image.png")
#blur image
blur_image = cv2.GaussianBlur(img, (7,7), 0)
#display the image
cv2.imshow('original Image', img)
cv2.imshow('Blur Image', blur_image)
cv2.waitKey(0)
