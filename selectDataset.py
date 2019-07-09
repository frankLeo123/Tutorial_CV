import cv2
import os

def select(inputPath,outPath):
    imgPath = os.listdir(inputPath)
    if not os.path.exists(outPath):
        os.mkdir(outPath)
    inNum = len(imgPath)
    for i in range(inNum):
        if i%10 ==0:
            print(imgPath[i])
            img = cv2.imread(inputPath+imgPath[i])
            cv2.imwrite(outPath+imgPath[i],img)

if __name__ == '__main__':
    dataset = ['ECSSD','DUT','SOD','HKU-IS','PASCALS']
    for data in dataset:
        inputPath = 'E:/dataset/4test/'+ data + '/gt/'
        outPath = 'E:/dataset/4test/'+ data + '/gtSelect/'
        # if not os.path.exists(outPath):
        #     os.mkdir(outPath)
        select(inputPath,outPath)
