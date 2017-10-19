# coding: utf-8
import DBController as DBC
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
db = DBC.DBManager()

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint != 'init' and request.endpoint != 'chkpw':
        return redirect(url_for('init'))

@app.route('/chkpw', methods=["POST"])
def chkpw():

    pw = request.form['pw']
    cnt = db.comparePW(pw)

    if cnt > 0:
        session['username'] = str(db.selectUserName())

    result = jsonify( {"result" : cnt})
    return result

@app.route('/changepw', methods=["POST"])
def updatepw():

    chpw = request.form['chpw']

    result = jsonify( {"result" : str(db.updatePW(chpw)) })
    return result

@app.route('/demo')
def demo():
    result = render_template('demo.html')
    return result

@app.route("/video")
def video():
    return render_template('video.html')

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

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True, host="0.0.0.0", port=8888, threaded = True)
    print("Server shutdown..")
