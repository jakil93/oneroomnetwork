#coding:utf-8

import RPi.GPIO as GPIO
import time

class ActuatorController:
    def __init__(self):

        self.buzzer_pin = 24

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.buzzer_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

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
    a.buzz_play(1)
    print("하하")
