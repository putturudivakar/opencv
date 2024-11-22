import cv2 as cv

img = cv.imread ('img5.jpg')
cv.imshow('group',img)


#converting to grayscale
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur',blur)


# edge cascade
canny = cv.Canny(img, 400,300)

cv.imshow("edge canny",canny) 

#Dilating image
dilated = cv.dilate(canny,(7,7), iterations=3 )
cv.imshow('dailated',dilated)

#eroding
eroded =cv.erode(dilated,(3,3), iterations=1)
cv.imshow('Eroded', eroded)


#resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)


#cropping
Cropped = img[50:200, 200:400]
cv.imshow('Cropped', Cropped)

cv.waitKey(0)