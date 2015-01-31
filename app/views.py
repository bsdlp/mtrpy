from app import app
from .mtrpy import MTR
from flask import render_template, request


@app.route('/')
def index():
    mtr = MTR(request)
    if mtr.is_curl or mtr.is_powershell:
        return mtr.report_mtr()
    else:
        return render_template('index.html')


@app.route('/mtrwindow')
def mtrwindow():
    mtr = MTR(request)
    return render_template(
        'mtrwindow.html', clientIP=mtr.client_ip,
        reportMTR=mtr.report_mtr())
