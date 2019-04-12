#!/usr/bin/env python3
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

try:
    app.config.from_object(os.environ['APP_SETTINGS'])
except:
    app.config.from_object('config.DevelopmentConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()