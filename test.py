import torch as t
import time
import numpy as np
import cv2
import scipy.misc
import matplotlib.pyplot as plt
# In [22]:
# a = t.arange(0, 6)
# # b = a.view(2, 3)
# # print(b)
# # # Out[22]:
# # tensor([[ 0.,  1.,  2.],
# #         [ 3.,  4.,  5.]])
# # # In [23]:
# b = a.view(-1, 3) # 当某一维为-1的时候，会自动计算它的大小
# # b.shape
# # # Out[23]:
# # torch.Size([2, 3])
# # # In [24]:
#  # 注意形状，在第1维（下标从0开始）上增加“１”
# # #等价于 b[:,None]
# c = b.view(1, 1, 1, 2, 3)
# c.squeeze(0) # 压缩第0维的“１”
# print(c.squeeze().size())
#

# 两种统计时间方法 + love小trick
# start = cv2.getTickCount()
# # start = time.clock()
# better_girl = 0
# love = False
# time_ = 1314
# if better_girl != 0:
#     print("I have no girlfriend,and I will have")
# else:
#     for i in range(time_):
#         if love == True:
#             print("I always have a girlfriend")
#         else:
#             print("I need find a better girl")
# # end =time.clock()
# end = cv2.getTickCount()
#
# time2 = start-end
# print('------------------'+str(time2/cv2.getTickFrequency()))

# img = cv2.imread("1.jpg",1)
#
# cv2.namedWindow("demo",cv2.WINDOW_NORMAL)
# cv2.imshow("demo",img)
# s = cv2.waitKey(50000)
#
# if s == ord('s'):
#     print("it's ok")
#     cv2.imwrite("./1.bmp",img)
# img = scipy.misc.face(gray=False)
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.subplot(121)
# plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
# plt.imshow(img)
# plt.subplot(122)
# plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
# plt.imshow(img1)
# plt.show()
# # cv2.namedWindow("22",cv2.WINDOW_NORMAL)
# cv2.imshow("22",img1)
# s = cv2.waitKey(10000)
# if s == ord('s'):
#     cv2.imwrite('successed.png',img1)




# img = scipy.misc.face(gray=True)

# img = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

# ret, thed = cv2.threshold(img,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)
# # thed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)
#
# # print(img.shape)
# plt.imshow(thed,cmap='gray')
# plt.show()
# cv2.imshow('demo',thed)
# cv2.waitKey(0)
# 缩放
# res = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
#
# # 反转
# # res = cv2.flip(img,-1)
#
# # 平移
# # row,col = img.shape[:2]
# # M = np.float32([[1,0,50],[0,1,100]])
# # res = cv2.warpAffine(img,M,(col,row))\
#
# row,col = img.shape[:2]
# M = cv2.getRotationMatrix2D((col/2, row/2),45,0.5)
# res = cv2.warpAffine(img,M,(col,row))
# cv2.imshow('demo',res)
# cv2.waitKey(0)

# img = np.zeros((400,300),dtype=np.uint8)
# # cv2.circle(img,(img.shape[1]//2,img.shape[0]//2),img.shape[1]//3,(255,0,0),thickness=-1)
# # cv2.putText(img,'test',(22,22),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
#
# point = np.array([[11,11],[101,101],[222,111],[222,222]],dtype=np.int32())
# pts = point.reshape((-1, 1, 2))
# cv2.polylines(img, [pts], True, (255, 255, 255))
# cv2.imshow("black",img)
# cv2.waitKey(0)

import cv2
import numpy as np
# drawing = False  # 是否开始画图
# mode = True  # True：画矩形，False：画圆
# start = (-1, -1)
# def mouse_event(event, x, y, flags, param):
#     global start, drawing, mode
#     # 左键按下：开始画图
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         start = (x, y)
#     # 鼠标移动，画图
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             if mode:
#                 cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
#             else:
#                 cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#     # 左键释放：结束画图
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode:
#             cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
#         else:
#             cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', mouse_event)
# while(True):
#     cv2.imshow('image', img)
#     # 按下m切换模式
#     if cv2.waitKey(1) == ord('m'):
#         mode = not mode
#     elif cv2.waitKey(1) == 27:
#         break

# draw = False
# start =(-1,-1)
# img = np.ones((300,400,3),dtype=np.uint8) * 255
# cv2.namedWindow("mouse")
#
# def nothing(x):
#     pass
#
# cv2.createTrackbar('color_R','mouse',0,255,nothing)
# cv2.createTrackbar('color_G','mouse',0,255,nothing)
# cv2.createTrackbar('color_B','mouse',0,255,nothing)
#
#
# def mouse_move(event,x,y,flag,param):
#     global draw,start,color
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # cv2.circle(img,(x,y),11,(255,255,255),-1)
#         draw = True
#         start = (x,y)
#         print(x,',',y)
#     elif event ==cv2.EVENT_MOUSEMOVE:
#         if draw ==True:
#             cv2.circle(img, (x,y), 11, color, -1)
#             # cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         draw = False
#         cv2.circle(img, (x, y), 11, color, -1)
#         # cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
#
#
# cv2.setMouseCallback('mouse',mouse_move)
# while (True):
#     r = cv2.getTrackbarPos('color_R','mouse')
#     g = cv2.getTrackbarPos('color_G','mouse')
#     b = cv2.getTrackbarPos('color_B','mouse')
#
#     color = (b,g,r)
#     print(color)
#     cv2.imshow('mouse',img)
#     if cv2.waitKey(1) == 27:
#         break

# img = scipy.misc.face(gray=True)
#
# # kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#
# _,thresh = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# image = cv2.merge((image,image,image))
# img = cv2.merge((img,img,img))
# cv2.drawContours(image,contours,-1,(0,0,255))
#
# res = np.hstack((img,image))
# cv2.imshow("res",res)
# cv2.waitKey(0)

img = cv2.imread('./debug/abc.jpg',0)

_,img = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
# cv2.imshow('demo',img_)
# cv2.waitKey(0)
image, contour, _ = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

a, b, c = contour[5], contour[1], contour[4]
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
image_ = np.copy(image)
cv2.drawContours(image_,contour,5,(0,0,255),5)
cv2.drawContours(image_,contour,1,(0,255,0),5)
cv2.drawContours(image_,contour,4,(255,0,0),5)

# cv2.imshow('demo',image_)
# cv2.waitKey(0)

# 面积
# area, arc = cv2.contourArea(a),cv2.arcLength(a,True)
# print(area,arc)

# 矩形
# x, y, w, h = cv2.boundingRect(a)
# cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),4)

# 圆形
# (x,y), radius  = cv2.minEnclosingCircle(a)
# x,y,radius = np.int0(x),np.int0(y),np.int0(radius)
# cv2.circle(image,(x,y),radius,(0,0,255),5)
# approx = cv2.approxPolyDP(contour[0],3,True)
approx = cv2.convexHull(b)
cv2.polylines(image, [approx], True , (0,0,255), 4)
cv2.imshow('rect',image)
cv2.waitKey(0)

# print(cv2.matchShapes(a, a, 1, 0.0))
# print(cv2.matchShapes(a, b, 1, 0.0))
# print(cv2.matchShapes(a, c, 1, 0.0))
