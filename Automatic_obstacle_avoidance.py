import RPi.GPIO as GPIO
import time
from carMove import CarMove
from infrared import Infrared

FPS2 = 0.1 * 1.4
FPS = 0.1


LEFTTIME = 0.2136
RIGHTTIME = 0.1461
LEFTTIME_MC = 0.0712
RIGHTTIME_MC = 0.0487


class Avoidance(CarMove, Infrared):
    def __init__(self):
        CarMove.__init__(self)
        Infrared.__init__(self)
        self.ahead_statue = self.Getahead()
        self.back_statue = self.Getback()
        self.side_statue = self.Getside()
        self.all_statue = self.Getall()
        self.lefttimes = 0
        self.righttimes = 0

    def update_ahead(self):
        self.ahead_statue = self.Getahead()

    def update_back(self):
        self.back_statue = self.Getback()

    def update_side(self):
        self.side_statue = self.Getside()

    def update_all(self):
        self.all_statue = self.Getall()

    def goahead(self):
        self.update_ahead()
        msgs = 'ok'
        while self.ahead_statue != "111":
            msgs = 'doit'
            self.update_ahead()
            if self.ahead_statue == "110":
                self.turnleft_and_go()
            elif self.ahead_statue == "101":
                self.turnfront_and_go()
            elif self.ahead_statue == "100":
                self.turnleftA_and_go()
            elif self.ahead_statue == "011":
                self.turnright_and_go()
            elif self.ahead_statue == "010":
                self.turnline()
            elif self.ahead_statue == "001":
                self.turnrightA_and_go()
            elif self.ahead_statue == "000":
                self.allstop()
        else:
            self.go()
            self.update_ahead()

        return msgs

    def go(self):
        self.update_ahead()
        if self.ahead_statue == "111":
            self.frontTime(FPS)
        else:
            return False

        return True

    def backleft(self):
        self.update_ahead()
        self.update_back()
        if self.back_statue == '1':
            self.leftRearTimes(FPS)
        else:
            return False
        return True

    def backright(self):
        self.update_ahead()
        self.update_back()
        if self.back_statue == '1':
            self.rightRearTimes(FPS)
        else:
            return False
        return True

    def back(self):
        self.update_back()
        if self.back_statue == '1':
            self.rearTime(0.05)
        else:
            return False
        return True

    def turnleft(self):
        self.update_ahead()
        if self.ahead_statue[1:] == '11':
            self.leftTime(FPS2)
        else:
            return False
        return True

    def turnright(self):
        self.update_ahead()
        if self.ahead_statue[0:2] == '11':
            self.rightTime(FPS)
        else:
            return False
        return True

    def turnlefts(self, times):
        self.update_ahead()
        if self.ahead_statue[1:] == '11':
            self.leftTime(times)
        else:
            return False
        return True

    def turnrights(self, times):
        self.update_ahead()
        if self.ahead_statue[0:2] == '11':
            self.rightTime(times)
        else:
            return False
        return True

    def turnleft_and_go(self):  # 右前方有障碍物  110
        self.update_ahead()
        times = 0
        # 第一步
        print("第一步")
        while self.ahead_statue != "111":
            self.update_ahead()
            time.sleep(0.2)
            if self.turnright():  # 左转 和 右转每fps 转动角度不一样
                times += 1
            else:
                return
            print("times =%d" % times)
            if times >= 9:
                return
        # 第二步 移动
        time.sleep(0.2)
        print("第二步")
        for i in range(2):
            if not self.go():
                return
        time.sleep(0.2)
        # 第三步 转弯
        print("第三步")
        for i in range(times * 2):
            time.sleep(0.2)
            if not self.turnleft():
                return

        time.sleep(0.2)
        # 第四步 移动
        print("第四步")
        for i in range(2):
            if not self.go():
                return
        # 第五步 转弯
        time.sleep(0.2)
        print("第五步")
        for i in range(times):
            time.sleep(0.2)
            if not self.turnright():
                return
        time.sleep(0.2)

    def turnleft_to_find_new_way(self):  # 在这一层， left 表示小车左侧的 轮子转动，这个函数完成小车向左转
        self.update_ahead()
        self.update_side()
        while self.ahead_statue[:2] != '11':
            self.update_ahead()
            self.update_side()
            time.sleep(0.1)
            self.update_side()
            self.backleft()
        times = 0
        time.sleep(0.1)
        while self.ahead_statue != '110':
            self.update_ahead()
            times += 1
            if self.turnright():
                time.sleep(0.1)
                self.go()
            if times >= 9:
                return
        time.sleep(0.2)

    def turnright_to_find_new_way(self):
        self.update_ahead()
        self.update_side()
        while self.ahead_statue != '111':
            self.update_ahead()
            self.update_side()
            time.sleep(0.1)
            self.back()
        times = 0
        while self.ahead_statue != '011':
            times += 1
            if self.turnleft():
                time.sleep(0.1)
                self.go()
            if times >= 20:
                return
        time.sleep(0.2)

    def turnback_and_left(self):
        self.update_side()
        while self.side_statue != '11':
            self.update_side()
            if not self.back():
                break
        time.sleep(0.2)

        for i in range(9):
            time.sleep(0.2)
            if not self.turnright():
                return
        time.sleep(0.2)
        for i in range(3):
            time.sleep(0.2)
            if not self.go():
                return
        time.sleep(0.2)

        for i in range(9):
            time.sleep(0.2)
            if not self.turnleft():
                return
        time.sleep(0.2)

    def turnfront_and_go(self):  # 正前方有障碍物 101
        self.update_side()
        if self.side_statue == '11':
            self.backleft()
        elif self.side_statue == '01':
            self.backright()
        elif self.side_statue == '10':
            self.backleft()
        else:
            self.turnback_and_left()

    def turnleftA_and_go(self):  # 前方和右方有障碍物 100
        self.backleft()
        time.sleep(0.2)
        self.turnleft_and_go()

    def turnright_and_go(self):  # 左前方有障碍物 011
        self.update_ahead()
        times = 0
        # 第一步
        print("第一步")
        while self.ahead_statue != "111":
            if self.turnleft():  # 左转 和 右转每fps 转动角度不一样
                time.sleep(0.2)
                times += 1
            else:
                return
            print("times =%d" % times)
            if times >= 9:
                return
        # 第二步 移动
        time.sleep(0.2)
        print("第二步")
        for i in range(2):
            time.sleep(0.2)
            if not self.go():
                return
        time.sleep(0.2)
        # 第三步 转弯
        print("第三步")
        for i in range(times * 2):
            time.sleep(0.2)
            if not self.turnright():
                return

        time.sleep(0.2)
        # 第四步 移动
        print("第四步")
        for i in range(2):
            time.sleep(0.2)
            if not self.go():
                return
        # 第五步 转弯
        time.sleep(0.2)
        print("第五步")
        for i in range(times):
            time.sleep(0.2)
            if not self.turnleft():
                return
        time.sleep(0.2)

    def turnline(self):  # 左右前方都有障碍物 010
        self.update_back()
        self.update_side()
        print("testA")
        if self.side_statue == "11":
            self.turnleft_to_find_new_way()
            print("testB")
        elif self.side_statue == "10":
            self.turnleft_to_find_new_way()
        elif self.side_statue == "01":
            self.turnright_to_find_new_way()
        else:
            self.turnback_and_left()

    def turnrightA_and_go(self):  # 左边和前边有障碍物 001
        self.backright()
        time.sleep(0.2)
        self.turnright_and_go()

    def allstop(self):  # 前方很危险 000
        self.update_back()
        self.update_side()
        if self.side_statue == "11":
            self.turnleft_to_find_new_way()
        elif self.side_statue == "10":
            self.turnleft_to_find_new_way()
        elif self.side_statue == "01":
            self.turnright_to_find_new_way()
        else:
            self.turnback_and_left()

    def Keep_turning_right(self):  # 按照正常的理解来，这个函数要实现小车向右转
        if not self.turnlefts(FPS2):
            if not self.back():
                self.go()

    def Keep_turning_left(self):
        if not self.turnrights(FPS):
            if not self.back():
                self.go()


if __name__ == "__main__":
    avoidance = Avoidance()
    while True:
        time.sleep(1)
        avoidance.goahead()
