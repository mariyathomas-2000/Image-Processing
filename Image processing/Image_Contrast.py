#Program to adjust image contrast
#import opencv and numpy
import cv2
import numpy as np
#read the original image
img = cv2.imread("image.png")
#to contrast the image
contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
#to display the image
cv2.imshow('Original Image', img)
cv2.imshow('Contrast Image', contrast_img)
cv2.waitKey(0)
