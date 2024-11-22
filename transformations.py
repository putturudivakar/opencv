import cv2 as cv 
import numpy as np
img = cv.imread('img5.jpg')
cv.imshow('group', img)


# Transalation
def translate(img, x,y):
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x-->left
# -y-->up
# x-->right
# y-->down
translated =translate(img, -100, 100)
cv.imshow('Transalated',translated)

# Rotation
def rotate(img, angle,rotpoint=None):
   (height,width) =img.shape[:2]

   if rotpoint is None:
      rotpoint = (width//2,height//2)

      rotMat =cv.getRotationMatrix2D(rotpoint, angle, 1.0)
      dimensions = (width,height)   
      return cv.warpAffine(img, rotMat, dimensions)   
rotated =rotate(img, -45)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('rotated_rotated',rotated_rotated)


#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)


#flipping
flip =cv.flip(img,1)
cv.imshow('flip',flip)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)