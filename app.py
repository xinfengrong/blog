
from flask import Flask
from flask_script import Manager
from App.views import blog
from App.ext import db,login_manager
from App.blog import *
from App.user import *
from flask_migrate import MigrateCommand, Migrate
app = Flask(__name__)
app.config.from_pyfile('setting.py')

db.init_app(app)

app.config.from_pyfile('setting.py')
# migrate=Migrate(db=db,app=app)
login_manager.init_app(app)
login_manager.login_view='/user/login/'

app.register_blueprint(blog)
app.register_blueprint(us)
manager = Manager(app)
# manager.add_command('dd',MigrateCommand)

if __name__ == '__main__':
    manager.run()

