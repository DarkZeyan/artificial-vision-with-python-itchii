import cv2 #Import the library

#We read the image

image = cv2.imread('./images/img1.jpg')

epn_chiquito = cv2.resize(image,(300,300))
npe = cv2.flip(epn_chiquito,0)
grayscale = cv2.cvtColor(epn_chiquito,cv2.COLOR_BGR2GRAY)

cv2.imshow('Image',grayscale)
cv2.waitKey(0)

cv2.destroyAllWindows