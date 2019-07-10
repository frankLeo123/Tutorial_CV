import cv2
import numpy as np

img = cv2.imread('./debug/lena.jpg',1)
face = cv2.imread('./debug/face.jpg',1)
h,w = face.shape[:2]
ret = cv2.matchTemplate(img,face,cv2.TM_CCOEFF)
_,_,_,max_loc = cv2.minMaxLoc(ret)
cv2.rectangle(img,(max_loc[0],max_loc[1]),(max_loc[0] + w,max_loc[1] + h),(0,0,255),2)
cv2.imshow("img",img)
cv2.waitKey(0)