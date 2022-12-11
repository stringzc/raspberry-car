import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Infrared(object):
    def __init__(self):
        self.GPIO_Front_Infrared = 13
        self.GPIO_LeftF_Infrared = 26
        self.GPIO_RightF_Infrared = 6
        self.GPIO_Left_Infrared = 5
        self.GPIO_Right_Infrared = 19
        self.GPIO_Back_Infrared = 20
        GPIO.setup(self.GPIO_Front_Infrared, GPIO.IN)
        GPIO.setup(self.GPIO_LeftF_Infrared, GPIO.IN)
        GPIO.setup(self.GPIO_RightF_Infrared, GPIO.IN)
        GPIO.setup(self.GPIO_Left_Infrared, GPIO.IN)
        GPIO.setup(self.GPIO_Right_Infrared, GPIO.IN)
        GPIO.setup(self.GPIO_Back_Infrared, GPIO.IN)

    def Getall(self):
        front_measure = GPIO.input(self.GPIO_Front_Infrared)
        leftf_measure = GPIO.input(self.GPIO_LeftF_Infrared)
        rightf_measure = GPIO.input(self.GPIO_RightF_Infrared)
        left_measure = GPIO.input(self.GPIO_Left_Infrared)
        right_measure = GPIO.input(self.GPIO_Right_Infrared)
        back_measure = GPIO.input(self.GPIO_Back_Infrared)
        return str(front_measure)+str(leftf_measure)+str(rightf_measure)+str(left_measure)+str(right_measure)+str(back_measure)

    def Getahead(self):
        front_measure = GPIO.input(self.GPIO_Front_Infrared)
        leftf_measure = GPIO.input(self.GPIO_LeftF_Infrared)
        rightf_measure = GPIO.input(self.GPIO_RightF_Infrared)
        return str(leftf_measure) + str(front_measure) + str(rightf_measure)

    def Getback(self):
        back_measure = GPIO.input(self.GPIO_Back_Infrared)
        return str(back_measure)

    def Getside(self):
        left_measure = GPIO.input(self.GPIO_Left_Infrared)
        right_measure = GPIO.input(self.GPIO_Right_Infrared)
        return str(left_measure) + str(right_measure)


if __name__ == "__main__":
    while True:
        infrared = Infrared()
        print(infrared.InfraredMeasure())
        time.sleep(0.5)
