import RPi.GPIO as GPIO
import time
import sys


# 定义Car类
class CarMove(object):
    def __init__(self):
        self.inx_pin = [21, 22, 23, 24]
        # self.inx_pin是控制端in的pin
        self.RightAhead_pin = self.inx_pin[0]
        self.RightBack_pin = self.inx_pin[1]
        self.LeftAhead_pin = self.inx_pin[2]
        self.LeftBack_pin = self.inx_pin[3]
        # 分别是右轮前进，右轮退后，左轮前进，左轮退后的pin
        self.setup()

    # setup函数初始化端口
    def setup(self):
        print("begin setup ena enb pin")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # 初始化使能端pin，设置成高电平
        pin = None
        for pin in self.inx_pin:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        # 初始化控制端pin，设置成低电平
        print("setup ena enb pin over")

    # fornt函数，小车前进
    def front(self):
        self.setup()
        GPIO.output(self.RightAhead_pin, GPIO.HIGH)
        GPIO.output(self.LeftAhead_pin, GPIO.HIGH)

    # 小车前进维持times
    def frontTime(self, times):
        self.setup()
        GPIO.output(self.RightAhead_pin, GPIO.HIGH)
        GPIO.output(self.LeftAhead_pin, GPIO.HIGH)
        time.sleep(times)
        self.setup()

    # leftFront函数，小车左拐弯
    def leftFront(self):
        self.setup()
        GPIO.output(self.RightAhead_pin, GPIO.HIGH)

    # 小车左拐弯持续times
    def leftTime(self, times):
        self.setup()
        GPIO.output(self.RightAhead_pin, GPIO.HIGH)
        time.sleep(times)
        self.setup()

    # rightFront函数，小车右拐弯
    def rightFront(self):
        self.setup()
        GPIO.output(self.LeftAhead_pin, GPIO.HIGH)

    # 小车右拐弯持续times
    def rightTime(self, times):
        self.setup()
        GPIO.output(self.LeftAhead_pin, GPIO.HIGH)
        time.sleep(times)
        self.setup()

    # rear函数，小车后退
    def rear(self):
        self.setup()
        GPIO.output(self.RightBack_pin, GPIO.HIGH)
        GPIO.output(self.LeftBack_pin, GPIO.HIGH)

    def rearTime(self, times):
        self.setup()
        GPIO.output(self.RightBack_pin, GPIO.HIGH)
        GPIO.output(self.LeftBack_pin, GPIO.HIGH)
        time.sleep(times)
        self.setup()

    # leftRear函数，小车左退
    def leftRear(self):
        self.setup()
        GPIO.output(self.RightBack_pin, GPIO.HIGH)

    def leftRearTimes(self, times):
        self.setup()
        GPIO.output(self.RightBack_pin, GPIO.HIGH)
        time.sleep(times)
        self.setup()

    # rightRear函数，小车右退
    def rightRear(self):
        self.setup()
        GPIO.output(self.LeftBack_pin, GPIO.HIGH)

    def rightRearTimes(self, times):
        self.setup()
        GPIO.output(self.LeftBack_pin, GPIO.HIGH)
        time.sleep(times)
        self.setup()


if __name__ == "__main__":
    car = CarMove()

    while True:
        car.leftTime(0.2136)
        time.sleep(1)
