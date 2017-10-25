import cv2

img = ''
cam = ''

def getImgStart():
    global img, cam
    cam = cv2.VideoCapture(0)
    while True:
        img = cam.read()[1]