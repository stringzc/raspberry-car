# 导入socket模块
import socket
from carMove import CarMove

IMAGESIZE = 921600
IMAGEWIDTH = 640
IMAFEHEIGHT = 480
FRAMELENGTH = 1024
LEFTTIME = 0.2136
RIGHTTIME = 0.1461
LEFTTIME_MC = 0.0712
RIGHTTIME_MC = 0.0487
if __name__ == '__main__':

    car = CarMove()

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_server.bind(("192.168.43.230", 10000))

    tcp_server.listen(128)

    tcp_client, tcp_client_address = tcp_server.accept()

    print("客户端的ip地址和端口号:", tcp_client_address)
    while True:
        recv_data = tcp_client.recv(1024)

        status = recv_data.decode(encoding="utf-8")
        print("接收客户端的数据为:", status)
        if status == "w":
            car.front()
        elif status == "wa":
            car.rightFront()
        elif status == "wd":
            car.leftFront()
        elif status == "s":
            car.rear()
        elif status == "sa":
            car.rightRear()
        elif status == "sd":
            car.leftRear()
        elif status == "p":
            car.setup()
        elif status == "rightrotate":
            car.leftTime(LEFTTIME)
        elif status == "leftrotate":
            car.rightTime(RIGHTTIME)
        elif status == "rmc":
            car.leftTime(LEFTTIME_MC)
        elif status == "lmc":
            car.rightTime(RIGHTTIME_MC)
