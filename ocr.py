import cv2, easyocr

reader = easyocr.Reader(['es','en'], gpu=False)

img = cv2.imread('./images/screenshot.png')

result = reader.readtext(img,)

for res in result:
    pt0 = res[0][0]
    
    pt1 = res[0][1]
    
    pt2 = res[0][2]
    
    pt3 = res[0][3]

    cv2.putText(img, res[1],(pt0[0],pt0[1]),2,0.8,(255,255,255),1)
    cv2.rectangle(img,pt0,pt2,(255,140,0),2)

cv2.imshow('Captura de pantalla',img)
cv2.waitKey(0)
cv2.destroyAllWindows()