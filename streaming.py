#coding:utf-8
import cv2
import imgs

def gen():
    try:
        while True:
            img = imgs.img
            frame=cv2.imencode(".jpeg",img)[1].tostring()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        del(cam)
    except:
        print("streaming 안 에러")