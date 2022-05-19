from flask import Flask
from flask_admin import Admin

from db import session
from settings import config

from components.users import admin as users_views
from components.students_bug import admin as students_bug_views
from components.students_met import admin as students_met_views
from flask_babelex import Babel

def admin_start():

    app = Flask(__name__)

    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        return 'ru'

    admin = Admin(app, name='GPK', template_mode='bootstrap3')

    users_views.load_views(admin, session)
    students_bug_views.load_views(admin, session)
    students_met_views.load_views(admin, session)

    app.config.from_object(config)
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
