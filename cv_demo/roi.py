import torch as t
import time
import numpy as np
import cv2
import scipy.misc
import matplotlib.pyplot as plt

img1 = cv2.imread('../debug/Lena.png')
img2 = cv2.imread('../debug/1.jpg')
# cv2.imshow('demo',img2)
# cv2.waitKey(0)
# row,col = img2.shape[:2]
# roi = img1[:row,:col]
#
# dst = cv2.addWeighted(roi,0.4,img2,0.6,0)
# cv2.imshow("addWeighted",dst)
# cv2.waitKey(0)
# 把logo放在左上角，所以我们只关心这一块区域
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]
# roi1 = np.zeros(img.shape[:2],dtype=np.uint8())
# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY)
mask = cv2.adaptiveThreshold(img2gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,6)

mask_inv = cv2.bitwise_not(mask)
img2_bg = cv2.bitwise_and(img2, img2, mask=mask_inv)
plt.subplot(221)
plt.imshow(mask_inv,cmap='gray')
plt.subplot(222)
plt.imshow(img2_bg[:,:,::-1])
# cv2.imshow("demo",mask_inv)
# cv2.waitKey(0)
# 保留除logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
dst = cv2.add(img1_bg, img2_bg)  # 进行融合
plt.subplot(223)
plt.imshow(img1_bg[:,:,::-1])
img1[:rows, :cols] = dst  # 融合后放在原图上
plt.subplot(224)
plt.imshow(dst[:,:,::-1])
plt.show()