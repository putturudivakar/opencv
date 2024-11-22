import cv2

#this function is used to read the image from location
img1 = cv2.imread('image2.jpg',1)
img1 = cv2.resize(img1,(1200,700))

cv2.imshow("read image",img1)






#grayscale, 0
img2 = cv2.imread('image2.jpg', 0)
img2 = cv2.resize(img2,(1200,700))
cv2.imshow("gray image",img2)
print("gray scale image value==\n",img2)



# blur , -1 in imread(image,-1)
img3 = cv2.imread('image2.jpg', -1)
img3 = cv2.resize(img3,(1200,700))
cv2.imshow("unchanged image",img3)
print("image orignal value==\n",img3)




cv2.waitKey(0)
cv2.destroyAllWindows()

















