import cv2
import numpy as np

img = np.zeros((400,400,3),dtype=np.uint8)
# img = np.zeros((400,400),dtype=np.uint8)

col,row = img.shape[:2]
print(col//8*3,row//8*5)

cv2.ellipse(img,(col//8*3,row//8*5),(col//8*1,col//8*1),0,0,300,(0,255,0),-1)
cv2.circle(img,(col//8*3,row//8*5),col//8* 2//4,(0,0,0),-1)

cv2.ellipse(img,(col//8*5,row//8*5),(col//8*1,col//8*1),0,300,600,(255,0,0),-1)
cv2.circle(img,(col//8*5,row//8*5),col//8* 2//4,(0,0,0),-1)

cv2.ellipse(img,(col//2,row//8*3),(col//8*1,col//8*1),0,120,420,(0,0,255),-1)
cv2.circle(img,(col//2,row//8*3),col//8*2//4,(0,0,0),-1)

cv2.imshow("demo",img)
cv2.waitKey(0)
cv2.imwrite('../debug/opencv_logo.png',img)