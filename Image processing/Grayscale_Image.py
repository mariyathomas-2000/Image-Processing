#convert image into grayscale(black &  white)
import cv2
img = cv2.imread("image.png")
#convert to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#display image
cv2.imshow("Gray scale image", gray_img)
cv2.waitKey(0)
