import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./debug/filter_input.bmp',1)

x0,y0 = 592 + 1 ,209 + 1
kSize = 2

# 选取roi np和cv相反
roi =img[(y0 - kSize):(y0 + kSize + 1),(x0 - kSize):(x0 + kSize + 1),:]
# roi =img[(y0 - 2*kSize):(y0 + 2*kSize + 1),(x0 - 2*kSize):(x0 + 2*kSize + 1),:]
# roi =img[(x0-2*kSize ):(x0+2*kSize),(y0-2*kSize):(y0+2*kSize),:]

# 验证roi
# cv2.rectangle(
#     img,(x0-2*kSize,y0-2*kSize),(x0 + 2*kSize,y0 + 2*kSize),(0,0,255),1
# )

# mean
mean_img = cv2.blur(img,(kSize,kSize))
mean_roi = mean_img[(y0 - kSize):(y0 + kSize + 1),(x0 - kSize):(x0 + kSize + 1),:]
res = list()
# 计算四个方向
direction = [[1,1],[0,1],[-1,1],[-1,0]]


for x,y in direction:
    value_f = mean_img[y0 + y * kSize,x0 + x * kSize,:]
    # value_f = mean_img[y0 + x * kSize,x0 + y * kSize,:]
    # value_f = mean_img[x0 + x * kSize,y0 + y * kSize,:]
    value_b = mean_img[y0 - y * kSize,x0 - x * kSize,:]
    # value_b = mean_img[y0 - x * kSize,x0 - y * kSize,:]

    # cv2.circle(img,(593 + -1 * kSize,210 + 1 * kSize),2,(0,0,255),-1)
    # cv2.circle(img,(593 - -1 * kSize,210 - 1 * kSize),2,(255,0,0),-1)

    # cv2.circle(img,(x0 + 1 * kSize,y0 + 1 * kSize),1,(0,0,255),1)
    # cv2.circle(img,(x0 - 1 * kSize,y0 - 1 * kSize),1,(255,0,0),1)
    # value_b = mean_img[x0 - x * kSize,y0 - y * kSize,:]
    print(value_f,'b:',value_b)
    # value_f.dtype = np.int8()
    # value_b.dtype = np.int8()
    # print(value_f/255.0,'b:',value_b/255.0)
    value_f = value_f/255.0
    value_b = value_b/255.0

    # print(value_f - value_b)
    res_ = (value_f - value_b)
    # print('res = ',res_)
    res.append(np.dot(res_,res_))


print(res)
# dst = np.hstack((mean_roi,roi))
dst = np.hstack((roi,mean_roi))
plt.xticks([])
plt.yticks([])
plt.imshow(dst[:,:,::-1])
plt.show()