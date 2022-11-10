import cv2
import numpy as np

black = np.zeros((512,512,3),dtype='uint8')

def draw(event,x,y,marks,params):    
        global drawing, x_value, y_value
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            x_value = x
            y_value = y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                cv2.rectangle(black,(x_value,y_value),(x,y),(255,140,0),-1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.rectangle(black,(x_value,y_value),(x,y),(255,140,0),-1)



#Se conecta la imagen con la funcion
cv2.namedWindow(winname='Circulo negro')
cv2.setMouseCallback('Circulo negro',draw)

#Show image while q key has not been pressed.
while True:
    cv2.imshow('Circulo negro',black)
    if cv2.waitKey(1) == ord('q') :
        cv2.destroyAllWindows()
        break
