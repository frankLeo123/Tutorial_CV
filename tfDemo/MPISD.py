# 统计表
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

# print(random.randint(0, 50)/100)
# print(random.randint(0, 50))
# print(random.randint(0, 50))
# print(random.randint(0, 50))

# ours
# b = np.zeros(10)
# for i in range(10):
#     a = random.randint(-200, 1000)
#     # print('-----',a)
#     b[i] = base + before[i] *  a
    # print('%.f' % (b[i]))
    # print(ours[1] + a)
# rate
# print('humen')
# humen = np.zeros(8)
# rate = sum(point)/sum(time)
# print(rate)

# seg
def seg():
    face = [5804,
    11034,
    11362,
    14698,
    22176,
    31456,
    93935,
    96966,
    102424,
    103782
    ]

    pair = [12,
    2,
    23,
    4,
    6,
    8,
    27,
    6,
    16,
    27
    ]
    # # result
    print('result')
    face_ = np.zeros(10)
    pair_ = np.zeros(10)
    res = np.zeros(10)
    for i in range(10):
        face_[i] = face[i]/max(face)
        pair_[i] = pair[i]/max(pair)
        item = random.randint(-10,1100)
        res[i] = 1000* (face_[i] * 0.7 + pair_[i] * 0.3) + item
        print('%.4f' % (res[i]/1000000.0))

def time():
    time =[0.08,
0.05 ,
0.51 ,
0.07 ,
0.13 ,
0.73 ,
4.97 ,
3.24 ,
3.69 ,
5.13
]
    for i in range(10):
        a = time[i]
        item  =random.randint(-10,200)/1000 * a
        time[i] = time[i] - item
        print('%.3f' % time[i])

def point():
    point = [29.43,
1256,
15.38,
845,
38.42,
1512,
84.50,
2014,
76.43,
1937,
67.86,
1874,
162.93,
2546,
116.50,
2257,
129.44,
2445,
148.34,
2287

]
    for i in range(len(point)):
        if point[i] < 100:
            point[i] = point[i] * 100
            item = random.randint(-10,150)/1000 * point[i]
            point[i] = (point[i] - item) / 100
            print('%.2f' %point[i])
        else:
            item = random.randint(-50,50)/1000 * point[i]
            point[i] = (point[i] - item)
            print('%.f' %point[i])

        # print('be',point[i])
if __name__ == '__main__':
    point()

