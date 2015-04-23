from app import app
from flask.ext.script import Manager

manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()