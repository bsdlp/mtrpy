#!/usr/bin/env python3.3
from flask.ext.script import Manager
import app

manager = Manager(app.app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()

