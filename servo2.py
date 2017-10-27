import RPi.GPIO as GPIO
import time

pin = 18  # PWM pin num 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0

try:
    while True:
        var = input("input : ")
        p.ChangeDutyCycle(int(var))
        print("angle :",int(var))
        time.sleep(1)
        p.stop()

except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()