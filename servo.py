import RPi.GPIO as GPIO
import time

pin = 18  # PWM pin num 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
cnt = 0

try:
    while True:
        p.start(0)
        var = input("input : ")
        p.ChangeDutyCycle(int(var))
        print("angle :",int(var))
        time.sleep(1)
        p.stop()

except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()