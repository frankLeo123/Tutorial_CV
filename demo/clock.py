import cv2
import numpy as np
import math
import datetime

img = np.ones((900,1200,3),dtype=np.uint8()) * 255

raw,col = img.shape[:2]

radius_clock = raw//9*4
radius_long = raw//30
radius_short = raw//100

print(raw,'q',col)

# # 画表盘
cv2.circle(img,(col//2,raw//2),radius_clock,(0,0,0),3)
for i in range(12):
    # i = 1
    x = col//2 + radius_clock * math.cos(i * math.pi / 6)
    y = raw//2 + radius_clock * math.sin(i * math.pi /6 )
    x1 = col//2 + (radius_clock - radius_long) * math.cos(i * math.pi / 6)
    y1 = raw//2 + (radius_clock - radius_long) * math.sin(i * math.pi /6 )
    x,y,x1,y1 = int(x),int(y),int(x1),int(y1)
    cv2.line(img,(x,y),(x1,y1),(0,0,0),thickness=4)

for i in range(60):
    x = col//2 + radius_clock * math.cos(i * math.pi / 30)
    y = raw//2 + radius_clock * math.sin(i * math.pi / 30)
    x1 = col//2 + (radius_clock - radius_short) * math.cos(i * math.pi / 30)
    y1 = raw//2 + (radius_clock - radius_short) * math.sin(i * math.pi / 30)
    x,y,x1,y1 = int(x),int(y),int(x1),int(y1)
    # line
    cv2.line(img,(x,y),(x1,y1),(0,0,0),3)


while(True):
    # 不断拷贝表盘图，才能更新绘制，不然会重叠在一起
    temp = np.copy(img)
    # 获取时间
    time = datetime.datetime.now()
    print(time)
    # print(time.hour,time.minute,time.second)
    # # 时钟
    x = col//2
    y = raw//2
    x1 = col//2 + (radius_clock - 7 * radius_long) * math.cos(math.fabs(time.hour - 12 + 9) * math.pi / 6)
    y1 = raw//2 + (radius_clock - 7 * radius_long) * math.sin(math.fabs(time.hour - 12 + 9) * math.pi /6 )
    x,y,x1,y1 = int(x),int(y),int(x1),int(y1)
    cv2.line(temp,(x,y),(x1,y1),(255,0,0),thickness=15)

    # # minute
    x = col//2
    y = raw//2
    minute = time.minute + 45 if time.minute <= 15 else time.minute - 15
    x1 = col//2 + (radius_clock - 5 * radius_long) * math.cos(minute * math.pi / 30)
    y1 = raw//2 + (radius_clock - 5 * radius_long) * math.sin(minute * math.pi / 30 )
    x,y,x1,y1 = int(x),int(y),int(x1),int(y1)
    cv2.line(temp,(x,y),(x1,y1),(0,255,0),thickness=8)

    # # second
    x = col//2
    y = raw//2
    second = time.second + 45 if time.second <= 15 else time.second - 15
    x1 = col//2 + (radius_clock - 3 * radius_long) * math.cos(second * math.pi / 30)
    y1 = raw//2 + (radius_clock - 3 * radius_long) * math.sin(second  * math.pi /30 )
    x,y,x1,y1 = int(x),int(y),int(x1),int(y1)
    cv2.line(temp,(x,y),(x1,y1),(0,0,255),thickness=4)

    # date
    str_time = str(time.day) + ' / ' + str(time.month) + ' / ' + str(time.year)
    cv2.putText(temp,str_time,(col//3,raw//3*2),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,25),thickness=3)

    cv2.imshow("demo",temp)
    if cv2.waitKey(1) == 27:
        break
    # cv2.waitKey(0)