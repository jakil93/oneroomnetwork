import RPi.GPIO as GPIO
import time

pin = 18  # PWM pin num 18

GPIO.setmode(GPIO.BCM)
# GPIO.setup(pin, GPIO.OUT)
cnt = 0
pre = 0

try:
    while True:
        GPIO.setup(pin, GPIO.OUT)
        p = GPIO.PWM(pin,50)
        p.start(0)
        var = input("input : ")
        if(pre != int(var)):
            p.ChangeDutyCycle(int(var))
            print("angle :",int(var))
        else:
            print("keep")
        pre = int(var)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()