# 创建两个滑动条分别调整对比度和亮度（对比度范围：0~0.3，亮度：0~100）。提示：因为滑动条没有小数，所以可以设置为0~300，然后乘以0.01。

import cv2
import numpy as np
import scipy.misc

img = scipy.misc.face(
    gray=False
)

def nothing(x):
    pass

cv2.namedWindow('light')
cv2.createTrackbar('a','light',0,300,nothing)
cv2.createTrackbar('b','light',0,50,nothing)
while (True):

    a_ = cv2.getTrackbarPos('a','light')
    b_ = cv2.getTrackbarPos('b','light')
    a = a_ * 0.01
    b = b_
    dst = np.array(np.clip((img * a + b),0,255),dtype=np.uint8())
    tmp = np.hstack((img,dst))

    cv2.imshow("light",tmp)
    if cv2.waitKey(1) == 27:
        break

