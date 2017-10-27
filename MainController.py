# coding: utf-8
import DBController as DBC
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response
from threading import Thread
import streaming as st
import picSetting
import directory
import motion
import imgs
import time
import json

app = Flask(__name__)
db = DBC.DBManager()

@app.before_request
def before_request():
    print("end", request.endpoint)
    if 'username' not in session and request.endpoint != 'init' and request.endpoint != 'chkpw' and request.endpoint != 'static':
        return redirect(url_for('init'))

@app.route('/getAlaramData', methods=["GET"])
def getAlaramData():

    data = db.selectAlaramData()
    print(data)
    print(u"------ 잘됬다.")

    datas = []
    datas.append({'no' : 1, 'subject' : "기상", 'time' : "07:00"})
    datas.append({'no' : 2, 'subject' : "출근", 'time' : "08:00"})

    return str(datas)



@app.route("/deleteAlaramData", methods=["POST"])
def deleteAlaramData():
    return jsonify({ 'result' : db.deleteAlaramData( request.form['no'] ) })

@app.route('/addAlaramData', methods=["POST"])
def addAlaramData():

    subject = request.form['subject']
    time = request.form['time']

    result = db.insertAlaramData(subject, time)
    no = db.getAlaramDataNo(subject, time)

    return jsonify({ 'result' : result.rowcount, "no" : no[0] })

@app.route('/chkpw', methods=["POST"])
def chkpw():

    pw = request.form['pw']
    cnt = db.comparePW(pw)

    if cnt > 0:
        print(str(db.selectUserName()))
        session['username'] = str(db.selectUserName())

    result = jsonify( {"result" : cnt})
    return result

@app.route('/changepw', methods=["POST"])
def updatepw():

    curpw = request.form['currentpw']
    chpw = request.form['chpw']

    result = jsonify( {"result" : str(db.updatePW(curpw, chpw)) })
    return result

@app.route('/demo')
def demo():
    result = render_template('demo.html')
    return result

@app.route("/record")
def record():
    return render_template('record.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/cctv')
def cctv():
    return render_template('cctv.html')

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

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/init')
def init():
    return render_template('init.html')

@app.route('/')
def index():
    result = render_template('init.html')

    if 'username' in session:
        result = render_template('main.html')
    return result

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
