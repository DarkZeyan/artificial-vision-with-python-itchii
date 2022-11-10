import cv2
import numpy as np

black = np.zeros((512,512,3),dtype='uint8')

img  = cv2.imread('./images/chocola.jpg')
chocoBig =  cv2.resize(img,(700,400))
cv2.rectangle(chocoBig,pt1=(180,50),pt2=(400,250),color=(255,30,0),thickness=5)

cv2.circle(black,center=(256,256),radius=100, color=(255,50,0),thickness=10)


font  = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(black, "ira we soy un circulo", org=(25,50),fontFace=font,fontScale=2,color=(150,90,100),thickness=3)




cv2.imshow('Chocola',chocoBig)
cv2.waitKey(0)

cv2.imshow('Black square',black)
cv2.waitKey(0)
cv2.destroyAllWindows()