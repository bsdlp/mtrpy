from app import app, mtrpy
from flask import render_template
from app.mtrpy import MTR


mtr = MTR()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mtrwindow')
def mtrwindow():
    mtr.get_client_ip()
    reportMTR = mtr.report_mtr(mtr.client_ip)
    return render_template('mtrwindow.html',
                           clientIP = mtr.client_ip,
                           reportMTR = reportMTR)

