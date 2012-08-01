from flask import Flask, request
from pbs import mtr

app = Flask(__name__)

@app.route('/')
def displayMTR():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = mtr("-r","-w",clientIP).stdout
    return "$ mtr -r -w " + clientIP + "\n" + reportMTR

@app.route('/mtrWindowRequest')
def displayMTRBrowser():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = mtr("-r","-w",clientIP).stdout
    return "<pre>$ mtr -r -w " + clientIP + "\n" + reportMTR + "</pre>"

@app.route('/4/<targetIP4>')
def displayMTRv4(targetIP4):
    reportMTR = mtr("-r","-w","-4",targetIP4).stdout
    return "$ mtr -r -w " + targetIP4 + "\n" + reportMTR

@app.route('/6/<targetIP6>')
def displayMTRv6(targetIP6):
    reportMTR = mtr("-r","-w","-6",targetIP6).stdout
    return "$ mtr -r -w " + targetIP6 + "\n" + reportMTR

@app.route('/ip/<targetIP>')
def displayMTRtarget(targetIP):
    reportMTR = mtr("-r","-w",targetIP).stdout
    return "$ mtr -r -w " + targetIP + "\n" + reportMTR

if __name__ == '__main__':
    app.run()