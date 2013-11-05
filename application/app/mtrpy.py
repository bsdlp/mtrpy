from sh import mtr
from flask import request

def mtrpy():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = mtr("-r","-w",clientIP, _bg=True)
    return reportMTR.wait()

