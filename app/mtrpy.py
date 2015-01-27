#!/usr/bin/env python3

from sh import mtr
from flask import request
import socket


class MTR(object):
    def __init__(self, client_ip=None, user_agent=None):
        self.user_agent = str(request.user_agent)
        self.get_client_ip()
        self.is_curl = self.is_curl()
        self.is_powershell = self.check_powershell()

    def get_client_ip(self):
        if not request.headers.getlist("X-Forwarded-For"):
            self.client_ip = request.remote_addr
        else:
            self.client_ip = request.headers.getlist("X-Forwarded-For")[-1]

    def check_curl(self):
        if "curl" in self.user_agent:
            return True
        else:
            return False

    def check_powershell(self):
        if "PowerShell" in self.user_agent:
            return True
        else:
            return False

    def report_mtr(self):
        report = mtr("--report-wide", self.client_ip, _bg=True)
        return report.wait()

