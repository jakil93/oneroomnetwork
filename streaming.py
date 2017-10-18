#coding:utf-8
import cv2


def gen():

    try:
        cam = cv2.VideoCapture(0)

        while True:
            ret, img = cam.read()
            frame=cv2.imencode(".mp4",img)[1].tostring()
            yield (b'--frame\r\n' b'Content-Type: video/mp4\r\n\r\n' + frame + b'\r\n')

        del(cam)
    except:
        print("streaming 안 에러")