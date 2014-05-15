from flask import Flask
from .mtrpy import MTR

app = Flask(__name__)
mtr = MTR()

from app import views, mtrpy

