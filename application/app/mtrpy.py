from sh import mtr
from flask import request

def mtrpy():
    """
    Janky-ass function for mtr via sh.
    """

    # janky-ass grab the user's ip addr
    if not request.headers.getlist("X-Forwarded-For"):
        clientIP = request.remote_addr
    else:
        clientIP = request.headers.getlist("X-Forwarded-For")[0]

    reportMTR = mtr("-r","-w",clientIP, _bg=True)
    return reportMTR.wait()

