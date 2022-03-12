import cv2

image = cv2.imread("solar-system.jpg")
cv2.putText(image,"Sun",(10,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Mercury",(100,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Venus",(180,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Earth",(280,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Mars",(380,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Jupiter",(520,240),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Saturn",(720,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Uranus",(950,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))
cv2.putText(image,"Neptune",(1090,150),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,255,255))

cv2.imshow("solar system",image)
cv2.waitKey(0)