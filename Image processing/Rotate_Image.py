#Rotating an image

import cv2
img = cv2.imread("image.png")
height, width = img.shape[0:2]

#to get the rotation matrix of our image
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
#rotate the image with the help of rotation matrix
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
#to show the image
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)
