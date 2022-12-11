import socket
import sys
import time


def start_tcp_client(ip, port):
    ###create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("start connect to server ")
        s.connect((ip, port))
    except socket.error:
        print("fail to connect to server")
    while True:
        print("connect success")
        time.sleep(1)
        msg = input("请输入命令")
        s.send(msg.encode('utf-8'))

        status = s.recv(1024)
        while status != b'ok':
            status = s.recv(1024)
        print(status)

    s.close()


if __name__ == '__main__':
    start_tcp_client('192.168.197.1', 10000)
