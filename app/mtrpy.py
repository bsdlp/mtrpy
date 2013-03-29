from sh import mtr
from flask import request

def mtrpy():
    clientIP = request.environ.get('REMOTE_ADDR')
    reportMTR = print mtr("-r","-w",clientIP)
    return reportMTR

