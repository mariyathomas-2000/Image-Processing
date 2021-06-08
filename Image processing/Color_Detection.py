#color detection
#program to detect green color from image
#import the modules cv2 for image and numpy for image array
import cv2
import numpy as np
#read the image and convert it  into HSV using cvtColor()
img = cv2.imread("color.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# create a NumPy array for the lowere green values and upper green values
lower_green = np.array([34, 177, 76])
upper_green = np.array([255, 255, 255])
#inRange method to check the image array elements lie between array values of
#upper and lower boundaries
#detect green color
masking = cv2.inRange(hsv_img, lower_green, upper_green)
#display image
cv2.imshow("original Image", img)
cv2.imshow("Green color detection", masking)
cv2.waitKey(0)
