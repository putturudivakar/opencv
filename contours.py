import cv2 as cv
import numpy as np

img = cv.imread('img5.jpg')
cv.imshow('buildings',img)

blank =np.zeros(img.shape,dtype='uint8')
cv.imshow('blank', blank)

gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(blur, 125,175)
cv.imshow("edge canny",canny) 


contours, hierarchies =cv.findContours(canny, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found")

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)