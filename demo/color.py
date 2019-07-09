import cv2
import numpy as np


# capture = cv2.VideoCapture(0)
# while(True):
#     # 获取一帧
#     ret, frame = capture.read()
#     # 将这帧转换为灰度图
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) == ord('q'):
#         break

# img = cv2.imread('Lena.png')
# # 转换为灰度图
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', img)
# cv2.imshow('gray', img_gray)
# cv2.waitKey(0)
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)


# 颜色转换
capture = cv2.VideoCapture('./debug/color.mp4')

lower_blue = np.array([0,110,110])
# lower_blue = np.array([85,110,110])
upper_blue = np.array([130,255,255])
while (capture.isOpened()):
    ret,frame = capture.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    # mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',frame)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    if cv2.waitKey(25) == 27: #esc
    # if cv2.waitKey(25) == ord('q'):
        break
#调整颜色
# ret,frame = capture.read()
# frame = cv2.imread('./debug/color.jpg',1)
# # plt.imshow(frame)
# # plt.show()
# blue = np.uint8([[[0, 0, 255]]])
# hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
# print(hsv_blue)  # [[[120 255 255]]]