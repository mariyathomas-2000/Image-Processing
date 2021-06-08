#program for  centroid detection
import cv2
img = cv2.imread("circle.png")
#convert to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#calculate the moment of image
moment = cv2.moments(gray_img)
#calculate the x and y coordinates of the center of the image
X = int(moment["m10"] /moment["m00"])
Y = int(moment["m01"] / moment["m00"])
#circule method to highlight the center position
cv2.circle(img, (X, Y), 15, (205, 114, 101), 1)
#display the image
cv2.imshow("Center of the Image", img)
cv2.waitKey(0)
