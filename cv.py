import cv2
import matplotlib.pyplot as plt
# capture = cv2.VideoCapture(0)
#
# while(capture.isOpened()):
#     ret,frame = capture.read()
#     width,height = capture.get(3),capture.get(4)
#     print(width,"*",height)
#     cv2.imshow("demo",frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# ret,frame = capture.start()
# import cv2
import numpy as np
# # 回调函数，x表示滑块的位置，本例暂不使用
# def nothing(x):
#     pass
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('image')
# # 创建RGB三个滑动条
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# while(True):
#     cv2.imshow('image', img)
#     if cv2.waitKey(1) == ord('q'):
#         break
#     # 获取滑块的值
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     # 设定img的颜色
#     img[:] = [b, g, r]
# def nothing(x):
#     pass
#
# img = np.zeros((300,512,3),dtype=np.uint8)
# cv2.namedWindow('image')
# cv2.createTrackbar('R','image',0,255,nothing)
#
# while(True):
#     cv2.imshow("image",img)
#     if cv2.waitKey(1) == ord('q'):
#         break
#     r = cv2.getTrackbarPos('R','image')
#     img[:] = [255,255,r]


# # perspective transform
# img = cv2.imread("./debug/warp.jpg",1)
#
# row,col = img.shape[:2]
# # print(row,':',col)
# x,y = col//3,row//3
# w = col//5
# h= w / 8.5 * 5.5
# point_before = np.array([[180,773],[2532,797],[772,1499],[2520,1617]],dtype=np.float32)
# point_new = np.array([[x,y],[x+w,y],[x,y+h],[x+w,y+h]],dtype=np.float32)
#
# M = cv2.getPerspectiveTransform(point_before, point_new)
#
# res = cv2.warpPerspective(img,M,(col,row))
#
# plt.xticks([])
# plt.yticks([])
# plt.subplot(211)
# plt.imshow(img[:,:,::-1])
# plt.subplot(212)
# plt.imshow(res[:,:,::-1])
# plt.show()


