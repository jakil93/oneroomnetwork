import cv2

# setup video capture
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

def gen():
    while True:
        ret,img = cam.read()
        jpegdata=cv2.imencode(".jpeg",img)[1].tostring()
        string = "--MjpgBound\r\n"
        string += "Content-Type: image/jpeg\r\n"
        string += "Content-length: "+str(len(jpegdata))+"\r\n\r\n"
        string += jpegdata
        string += "\r\n\r\n\r\n"
        yield string