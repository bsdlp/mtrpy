from flask import render_template
from app import app, mtrpy


@app.route('/')
def index():
    return render_template('index.html')

