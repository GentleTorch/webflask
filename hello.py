from flask.ext.script import Manager

from flask.ext.bootstrap import Bootstrap
from main import app


bootstrap=Bootstrap(app)

manager=Manager(app)

if __name__=='__main__':
    manager.run()