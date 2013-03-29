from flask import render_template
from sh import mtr
from app import app

@app.route('/')
def displayMTR():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = print(mtr("-r","-w",clientIP))
    return "$ mtr -r -w " + clientIP + "\n" + reportMTR

@app.route('/mtrWindowRequest')
def displayMTRBrowser():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = print(mtr("-r","-w",clientIP))
    return "<pre>$ mtr -r -w " + clientIP + "\n" + reportMTR + "</pre>"

@app.route('/4/<targetIP4>')
def displayMTRv4(targetIP4):
    reportMTR = print(mtr("-r","-w","-4",targetIP4))
    return "$ mtr -r -w " + targetIP4 + "\n" + reportMTR

@app.route('/6/<targetIP6>')
def displayMTRv6(targetIP6):
    reportMTR = print(mtr("-r","-w","-6",targetIP6))
    return "$ mtr -r -w " + targetIP6 + "\n" + reportMTR

@app.route('/ip/<targetIP>')
def displayMTRtarget(targetIP):
    reportMTR = print(mtr("-r","-w",targetIP))
    return "$ mtr -r -w " + targetIP + "\n" + reportMTR

@app.route('/targetForm')
def targetForm():
    clientIP = request.environ.get('REMOTE_ADDR')
    remoteTarget = request.args.get('remoteTarget', clientIP, type=str)
    reportMTR = print(mtr("-r","-w",remoteTarget))
    return "<pre>$ mtr -r -w " + remoteTarget + "\n" + reportMTR + "</pre>"

if __name__ == '__main__':
    app.run()
