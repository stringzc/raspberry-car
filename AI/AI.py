import socket
import sys
import time
from detect import Model
import cv2

low_bound = 900000
up_bound = 960000


def start_tcp_client(ip, port):
    stat = time.time()
    ###create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("start connect to server ")
        s.connect((ip, port))
    except socket.error:
        print("fail to connect to server")

    model = Model()
    video = cv2.VideoCapture("http://192.168.43.230:8000/stream.mjpg")

    # while True:
    #     ret, frame = video.read()
    #     c = cv2.waitKey(1)
    #     if c == 27:
    #         break
    #     model.detect(frame)
    #     if model.is_object():
    #         t = model.get_pos()[0]
    #         print(t, abs(t[2] - t[0]) * abs(t[3] - t[1]), model.where())
    #     model.draw()
    #     cv2.imshow("A video", frame)

    flag = False
    times = 0
    while True:
        print("connect success")
        ret, frame = video.read()
        c = cv2.waitKey(1)
        if c == 27:
            break
        msg = 'c'
        model.detect(frame)
        model.draw()
        cv2.imshow("A video", frame)
        T = model.has_object
        if T or flag:
            flag = True
            msgs = model.where()
            if msgs == 'right':
                print("too right")
                msg = 'rightrotate'
                # msg = 'leftrotate'
            elif msgs == 'left':
                # msg = 'rightrotate'
                print("too left")
                msg = 'leftrotate'
            else:
                if T:
                    times = 0
                    t = model.get_pos()[0]
                    area = abs(t[2] - t[0]) * abs(t[3] - t[1])

                    if low_bound <= area <= up_bound:
                        pass
                    elif area < low_bound:
                        msg = 'go'
                    else:
                        msg = 'rear'
                else:
                    times += 1
        elif not flag:
            msg = 'rightrotate'
        if times >= 5:
            flag = False
            times = 0
        # time.sleep(1)
        ends = time.time()
        if ends - stat >= 2:
            s.send(msg.encode('utf-8'))
            stat = time.time()
            status = s.recv(1024)
            print(status)
            if status == b'doit':
                flag = False

    s.close()
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    start_tcp_client('192.168.43.230', 10000)
