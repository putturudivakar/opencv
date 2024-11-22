
import cv2
import numpy as np

img = cv2.imread('image1.jpg')
blank = np.zeros((500,500,3),dtype='uint8')
cv2.imshow('blank',blank)                     #output black sheet image

#draw rectangle
cv2.rectangle(blank, (0,0), (250,250), (0,225,0), 3)

cv2.imshow('rectangle', blank)

#draw circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), -1)

cv2.imshow('circle', blank)

#text on image
cv2.putText(blank, 'my name is divakar',(0,350),cv2.FONT_HERSHEY_TRIPLEX, 1, (0,255,0), 1)

cv2.imshow('text', blank)

img = cv2.resize(img,(600,700))


#draw line
cv2.line(blank, (0,0), (400,400), (10, 92, 300), 3)
cv2.arrowedLine(blank, (0,50), (410,450), (0, 10, 200), 3) #arrow line

cv2.imshow('line', blank)


#print image certain colour
blank[200:300, 300:400] = 0,100,0   # change colour and inside small block
cv2.imshow('colour',blank)





img = cv2.imshow("shape_line",img)

cv2.waitKey(0)


