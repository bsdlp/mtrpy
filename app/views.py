from app import app, mtr
from flask import render_template


@app.route('/')
def index():
    mtr.get_user_agent()
    mtr.get_client_ip()
    if mtr.is_curl() or mtr.is_powershell():
        reportMTR = mtr.report_mtr(mtr.client_ip)
        return reportMTR
    else:
        return render_template('index.html')

@app.route('/mtrwindow')
def mtrwindow():
    mtr.get_client_ip()
    reportMTR = mtr.report_mtr(mtr.client_ip)
    return render_template('mtrwindow.html',
                           clientIP = mtr.client_ip,
                           reportMTR = reportMTR)

@app.route('/sup')
def sup():
    return "sup"

