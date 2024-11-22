import cv2 as cv 
import numpy as np

img =cv.imread('img5.jpg')
cv.imshow('group', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('average blur',average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3),0)
cv.imshow('gaussian blur',gauss)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur',bilateral)

cv.waitKey(0)