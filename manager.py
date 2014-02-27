#!/usr/bin/env python3
from flask.ext.script import Manager
import app

manager = Manager(app.app)

if __name__ == "__main__":
    manager.run()

