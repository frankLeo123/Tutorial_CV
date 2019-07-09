import cv2
import numpy as np
def nothing(x):
    pass

img = cv2.imread('../debug/circle_ring.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # 1 官方解决方案
_,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 默认
image,contours,hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 清晰
# image,contours,hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

image_ = np.copy(img)

# 填充，第一步完成
# cv2.drawContours(image_,contours,2,(215, 215, 180),-1)
# cv2.drawContours(image_,contours,4,(215, 215, 180),-1)
# cv2.drawContours(image_,contours,6,(215, 215, 180),-1)

# 勾勒轮廓，为了接下来处理
cv2.drawContours(image_,contours,2,(0, 0, 255),2)
cv2.drawContours(image_,contours,4,(0, 0, 255),2)
cv2.drawContours(image_,contours,6,(0, 0, 255),2)

cv2.imshow("demo",image_)
cv2.waitKey(0)


# # 2 自定义用hough解决
contour = image_[:,:,2]
mask = cv2.inRange(contour,254,255)
cv2.imshow("demo",mask)
cv2.waitKey(0)
mask_canny = cv2.Canny(mask,100,30)
dst = np.hstack((mask_canny,mask))
cv2.namedWindow("circle")
cv2.createTrackbar('param1','circle',120,200,nothing)
cv2.createTrackbar('param2','circle',12,200,nothing)
cv2.createTrackbar('minRadius','circle',22,30,nothing)
cv2.createTrackbar('maxRadius','circle',43,100,nothing)

while (True):
    image1 = np.copy(img)
    # 137 33 24 44
    param1 = cv2.getTrackbarPos('param1', 'circle')
    param2 = cv2.getTrackbarPos('param2', 'circle')
    minRadius = cv2.getTrackbarPos('minRadius', 'circle')
    maxRadius = cv2.getTrackbarPos('maxRadius', 'circle')
    circle = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,5,param1=param1,param2=param2,minRadius=minRadius,maxRadius=maxRadius)

    num_circle = 0
    if circle is not None:
        circle = np.uint16(np.around(circle[0,:,:]))
        for i in circle[:]:
            # Draw outer circle
            cv2.circle(image1, (i[0], i[1]), i[2], (215, 215, 180), -1)
            # Draw inner circle
            cv2.circle(image1, (i[0], i[1]), 2, (215, 215, 180), -1)
            num_circle = num_circle + 1
        print(num_circle)

    cv2.imshow('circle',image1)
    if cv2.waitKey(1) == 27:
        break