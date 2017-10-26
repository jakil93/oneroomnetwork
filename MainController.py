# coding: utf-8
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response
from threading import Thread
import streaming as st
import picSetting
import directory
import motion
import imgs
import time

app = Flask(__name__)


@app.route("/record")
def record():
    return render_template('record.html')

@app.route('/streaming')
def streming():
    return render_template('streaming.html')

@app.route('/video_feed')
def video_feed():
    img = st.gen()

    try:
        result = Response(img, mimetype='multipart/x-mixed-replace; boundary=frame')
    except:
        print("error")
        result = None

    return result

@app.route('/videoList')
def videoList():
    list = {'video' : directory.getList()}
    return jsonify(list)

@app.before_first_request
def setting():
    th1 = Thread(target=imgs.getImgStart)
    th1.daemon = True
    th1.start()

    time.sleep(0.5)

    motion.setting()
    th2 = Thread(target=motion.start)
    th2.daemon = True
    th2.start()

if __name__ == "__main__":
    picSetting.setting()
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True, host="0.0.0.0", port=8888)
    print("Server shutdown..")
