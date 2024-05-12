import cv2 

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"Earth",(290,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Moon",(325,150),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.35,color=(255,255,255))
cv2.putText(img,"Mars",(390,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(190,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(100,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(760,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"Jupiter",(540,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"Uranus",(940,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"Pluto",(1100,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(255,255,255))

cv2.imwrite("solar-system-with-text.jpg",img)
cv2.imshow("solar system",img)
cv2.waitKey(0)