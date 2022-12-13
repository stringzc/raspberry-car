import torch
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time


class Model:
    def __init__(
            self,
            modelPath='./yolov5',
            weightPath='weights/best.pt',
            # weightPath='weights/yolov5n.pt',
            conf=0.5):
        self.model = torch.hub.load(modelPath,
                                    'custom',
                                    weightPath,
                                    source='local')
        self.model.conf = conf
        self.has_apple = False
        self.img = None
        self.df = None
        self.place = None  # 记录物体的位置，分别记录左上角和右下角坐标

    # 预测物体
    def detect(self, img):
        self.img = img
        im = img[..., ::-1]
        self.df = self.model(im, size=640).pandas().xyxy[0]
        self.sz = img.shape  # 图像尺寸大小

        self.has_object = False
        self.place = []

        for i in range(len(self.df)):
            t = self.df.iloc[i]
            # print(self.df.iloc[i]['name'])
            if self.df.iloc[i]['name'] == 'banana':
                self.place.append([
                    int(t['xmin']),
                    int(t['ymin']),
                    int(t['xmax']),
                    int(t['ymax']),
                    np.around(t['confidence'], 2)
                ])
                self.has_object = True

    # 获取物体位置
    def get_pos(self):
        return self.place  # [xmin, ymin, xmax, ymax, conf]

    # 目标在图像中的位置
    def where(self):
        if self.place:
            pos = self.place[0]
            # 物体中心位置
            mid = (pos[0] + pos[2]) // 2
            if mid < self.sz[1] // 3:
                # print("left")
                return "left"
            elif mid > 2 * self.sz[1] // 3:
                # print("right")
                return "right"
            else:
                # print("mid")
                return 'mid'
        else:
            return 'mid'

    # # 判断当前画面是否有物体
    # def is_object(self):
    #     return self.object

    # 绘制矩形框
    def draw(self):
        if not self.has_object:
            print("there is no banana")
            return

        for pos in self.place:
            cv2.rectangle(self.img, (pos[0], pos[1]), (pos[2], pos[3]),
                          (0, 255, 0), 20)
            out = 'banana' + str(pos[4])
            cv2.putText(self.img, out, (pos[0], pos[1]),
                        cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 12)


# def main():
#     model = Model()
#     im = cv2.imread('./image/image_9.jpg')
#
#     start = time.time()
#     model.detect(im)
#     model.draw()
#     model.where()
#     end = time.time()
#     print("time:", end - start)
#     # while True:
#     #     cv2.imshow('pic', im)
#
#
# if __name__ == "__main__":
#     main()