#coding:utf-8

import RPi.GPIO as GPIO
import time, Adafruit_DHT, sys

class ActuatorController:
    def __init__(self):

        #init
        GPIO.setwarnings(False)
        GPIO.cleanup()

        #set pin
        self.dht_pin = 23
        self.buzzer_pin = 24
        self.servo_pin = 18
        self.dc_pin1 = 20
        self.dc_pin2 = 21
        self.current_curtain = "";

        #set etc
        self.dht_sensor = Adafruit_DHT.DHT11

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.buzzer_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        GPIO.setup(self.servo_pin, GPIO.OUT)

        GPIO.setup(self.dc_pin1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.dc_pin2, GPIO.OUT, initial=GPIO.LOW)

        self.p = GPIO.PWM(self.servo_pin, 50)
        self.p.start(4)
        self.p.ChangeDutyCycle(2)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)

    def curtainUp(self):
        GPIO.output(self.dc_pin1, 1)
        time.sleep(1.2)
        GPIO.output(self.dc_pin1, 0)

    def curtainDown(self):
        GPIO.output(self.dc_pin2, 1)
        time.sleep(1.2)
        GPIO.output(self.dc_pin2, 0)

    def doServo(self, angle):
        self.p.ChangeDutyCycle(angle)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)

    def closeWindow(self):
        self.p.ChangeDutyCycle(2)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)

    def openWindow(self):
        self.p.ChangeDutyCycle(10)
        time.sleep(1)
        self.p.ChangeDutyCycle(0)

    def getDHTInfo(self):
        humi, temp = Adafruit_DHT.read_retry(self.dht_sensor, self.dht_pin)

        while(humi is None):
            print("getDHTInfo 재시도..")
            humi, temp = Adafruit_DHT.read_retry(self.dht_sensor, self.dht_pin)

        return humi, temp


    def buzz(self, pitch, duration):
        if pitch == 0:
            time.sleep(duration)
            return
        period = 1.0 / pitch
        delay = period / 2
        cycles = int(duration * pitch)

        for i in range(cycles):
            GPIO.output(self.buzzer_pin, True)
            time.sleep(delay)
            GPIO.output(self.buzzer_pin, False)
            time.sleep(delay)

    def buzz_play(self, tune):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        x = 0

        if tune == 1:
            pitches = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1047]
            duration = 0.1

            for p in pitches:
                self.buzz(p, duration)
                time.sleep(duration * 0.5)
            for p in reversed(pitches):
                self.buzz(p, duration)
                time.sleep(duration * 0.5)

        elif tune == 2:
            pitches = [262, 330, 392, 523, 1047]
            duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0, 5]

            for p in pitches:
                self.buzz(p, duration[x])  # feed the pitch and duration to the function, “buzz”
                time.sleep(duration[x] * 0.5)
                x += 1
        elif tune == 3:
            pitches = [392, 294, 0, 392, 294, 0, 392, 0, 392, 392, 392, 0, 1047, 262]
            duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.4]
            for p in pitches:
                self.buzz(p, duration[x])  # feed the pitch and duration to the func$
                time.sleep(duration[x] * 0.5)
                self.buzz(p, duration[x])  #feed the pitch and duration to the func$
                time.sleep(duration[x] *0.5)
                x+=1
        elif tune == 4:
            pitches=[1047, 988,659]
            duration=[0.1,0.1,0.2]
            for p in pitches:
                self.buzz(p, duration[x])  #feed the pitch and duration to the func$
                time.sleep(duration[x] *0.5)
                x+=1
        elif(tune==5):
            pitches=[1047, 988,523]
            duration=[0.1,0.1,0.2]
            for p in pitches:
                self.buzz(p, duration[x])  #feed the pitch and duration to the func$
                time.sleep(duration[x] *0.5)
                x+=1

        GPIO.setup(self.buzzer_pin, GPIO.IN)

if __name__ == "__main__":
    a = ActuatorController()

    # a.buzz_play(2)
    # print("하하")

    print(a.getDHTInfo())
    # while True:
    #     try:
    #         cnt = input("open : 1, close : 0 \n")
    #         if(cnt == 1):
    #             a.openWindow()
    #         elif(cnt == 0):
    #             a.closeWindow()
    #     except :
    #         break;

    while True:
        try:
            cnt = input("Up : 1, Down : 0 \n")
            if(cnt == 1):
                print(1)
                a.curtainUp()
            elif(cnt == 0):
                print(0)
                a.curtainDown()
        except :
            break;


        