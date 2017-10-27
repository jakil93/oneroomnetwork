import RPi.GPIO as GPIO
import time
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin,50)
p.start(12.5)
time.sleep(0.5)
p.stop()
p.start(7.5)
time.sleep(0.5)
p.stop
p.start(10.0)
time.sleep(0.5)
p.stop()
var = 1
try:
    while True:
        var = input("input : ")
        p.start(var)
        time.sleep(1)
        p.stop()

except KeyboardInterrupt:
    GPIO.cleanup()