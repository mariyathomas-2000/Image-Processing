#program to crop an image
import cv2
img = cv2.imread("image.png")
height, width = img.shape[0:2]
#define the size of the newly created image
startRow = int(height*.15)
startCol = int(width*.15)
endRow = int(height*.85)
endCol = int(width*.85)
#specifing the range from starting to ending of rows and coloms
croppedImage = img[startRow:endRow, startCol:endCol]
#display the original and cropped image
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', croppedImage)
cv2.waitKey(0)
