#coding:utf-8
import time
from datetime import datetime
import cv2
import imgs
from threading import Thread

thresh = 52
fourcc = ''

img = ''
i0 = ''
i1 = ''
i2 = ''
set = False
fr = 26


def diffImage(i0, i1, i2):
    diff0 = cv2.absdiff(i0, i1)
    diff1 = cv2.absdiff(i1, i2)
    return cv2.bitwise_and(diff0, diff1)

def getImg():
    global i0, i1, i2

    img = imgs.img

    if(set):
        i0 = i1
        i1 = i2
        i2 = grayImg(img)

    return img

def grayImg(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return gray

def recording(frames):
    cnt = 0
    while cnt < fr*5:
        frames.append(getImg())
        time.sleep(float(1) / float(fr))
        cnt += 1
    print(len(frames))

    return frames

def release(out, frames):
    t = time.time()
    print("release start")
    for frame in frames:
        out.write(frame)
    out.release()
    t = time.time() - t
    print("release stop : ",t)

def getOutput(frame):
    h, w, _ = frame.shape
    out = cv2.VideoWriter('static/video/' + str(datetime.now().strftime('%Y-%m-%d:%H%M%S')) + '.mp4', fourcc, fr, (w, h), True)
    return out

def motionCheck():
    diff = diffImage(i0, i1, i2)
    ret, thrimg = cv2.threshold(diff, thresh, 1, cv2.THRESH_BINARY)
    count = cv2.countNonZero(thrimg)

    return count

def setting():
    global fourcc, i0, i1, i2, img, set
    fourcc = cv2.VideoWriter_fourcc(*"H264")

    i0 = grayImg(getImg())
    i1 = grayImg(getImg())
    img = getImg()
    i2 = grayImg(img)

    set = True


def start():
    global i0, i1, i2, img

    while True:
        count = motionCheck()
        if(count > 1):
            frames = []
            tt = time.time()
            print('시작')
            out = getOutput(img)
            while True:
                frames = recording(frames)
                count = motionCheck()
                if not(count > 1):
                    # th = Thread(target=release, args=(out, frames))
                    # th.start()
                    release(out, frames)

                    print('종료')
                    tt = time.time() - tt
                    print('time :', tt)
                    break
                else:
                    print('계속')

        getImg()