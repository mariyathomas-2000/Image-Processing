#program to remove background from an image
import cv2
import numpy as np
#read image convert to grayscale
img = cv2.imread("background.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#find the threshold
_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#find the image contours
img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
#Sort the contours
img_contours= sorted(img_contours, key=cv2.contourArea)
for i in img_contours:
    if cv2.contourArea(i) > 100:
        break
#generate the mask using np.zeros
mask = np.zeros(img.shape[:2], np.uint8)
#draw contour
cv2.drawContours(mask, [i],-1, 255, -1)
#apply the bitwise_and operator
new_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("original Image", img)
cv2.imshow("Image with background removed", new_img)
cv2.waitKey(0)
