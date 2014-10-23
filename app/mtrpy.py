#!/usr/bin/env python3

from sh import mtr
from flask import request
import socket


class MTR(object):
    def __init__(self, client_ip=None, user_agent=None):
        self.client_ip = client_ip
        self.user_agent = user_agent

    def get_user_agent(self):
        self.user_agent = str(request.user_agent)

    def get_client_ip(self):
        if not request.headers.getlist("X-Forwarded-For"):
            self.client_ip = request.remote_addr
        else:
            self.client_ip = request.headers.getlist("X-Forwarded-For")[-1]

    def is_curl(self):
        if "curl" in self.user_agent:
            return True
        else:
            return False

    def is_powershell(self):
        if "PowerShell" in self.user_agent:
            return True
        else:
            return False

    def lookup(self, addr):
        try:
            return socket.gethostbyaddr(addr)
        except socket.herror:
            return 'No PTR record for %s' % addr

    def report_mtr(self, addr):
        if self.client_ip:
            report = mtr("--report-wide", self.client_ip, _bg=True)
        else:
            report = mtr("--report-wide", addr, _bg=True)
        return report.wait()

