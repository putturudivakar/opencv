import cv2 as cv

img = cv.imread ('img5.jpg')
cv.imshow('group',img)


gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Simple thresholding
threshold, thresh = cv.threshold(gray, 150 ,255,cv.THRESH_BINARY)
cv.imshow('Simple trash',thresh)

threshold, thresh_inv = cv.threshold(gray, 150 ,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple trash inverse',thresh_inv)

#Adoptive Threshholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive thresholding', adaptive_thresh)

cv.waitKey(0)