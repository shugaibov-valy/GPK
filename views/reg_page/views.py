from flask import render_template, request
from flask.views import MethodView
from components.users.models import User


class RegView(MethodView):
    def get(self):
        return render_template('pages/reg_page/index.html')

    def post(self):
        login = request.form.get('login')
        password = request.form.get('password')
        conf_password = request.form.get('conf_password')
        enum = request.form.get('enum')
        message = ""
        if password != conf_password:
            return render_template('pages/reg_page/index.html', message="Пароли не совпадают!")
        else:
            User.create_user(login, password, enum)
            return render_template('pages/reg_page/index.html', message="Пользователь создан!")
