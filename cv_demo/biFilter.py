import numpy as np
import cv2

def nothing(x):
    pass
img = cv2.imread('../debug/Lena.png',1)
cv2.namedWindow('bilatera')
cv2.createTrackbar('color','bilatera',1,200,nothing)
cv2.createTrackbar('space','bilatera',1,200,nothing)


while (True):
    color = cv2.getTrackbarPos('color','bilatera')
    space = cv2.getTrackbarPos('space','bilatera')
    # res = cv2.GaussianBlur(img,(5,5),1)
    # res = cv2.medianBlur(img,9)
    res = cv2.bilateralFilter(img,9,color,space)
    dst = np.hstack((img,res))
    cv2.imshow("bilatera",dst)
    if cv2.waitKey(1) == 27:
        break
    # plt.imshow(dst[:,:,::-1])
    # plt.show()