from flask import Flask, request
from pbs import mtr

app = Flask(__name__)

def clientIP():
	userIP = request.environ.get('REMOTE_ADDR')
	return userIP

@app.route('/')
def displayMTR():
	clientIP = clientIP()
	reportMTR = mtr("-r","-w",clientIP).stdout
	return "<pre>" + reportMTR + "</pre>"

@app.route('/c')
def displayMTRBrowser():
	clientIP = clientIP()
	reportMTR = mtr("-r","-w",clientIP).stdout
	return reportMTR

@app.route('/c4')
def displayMTRv4():
	clientIP = clientIP()
	reportMTR = mtr("-r","-w","-4",clientIP).stdout
	return reportMTR

@app.route('/c6')
def displayMTRv4():
	clientIP = clientIP()
	reportMTR = mtr("-r","-w","-6",clientIP).stdout
	return reportMTR

if __name__ == '__main__':
	app.run()