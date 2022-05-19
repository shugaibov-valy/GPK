from flask import redirect, render_template, request, session
from components.users import exc
from components.users.models import User
from flask.views import MethodView



class AuthView(MethodView):

    def get(self):
        return render_template("pages/auth_page/index.html")

    def post(self):
        login_form = request.form.get('login')
        password_form = request.form.get('password')
        try:
            user = User.login_check(login_form, password_form)
            session["login"] = user.login
            session["enum"] = user.enum
            return redirect("/main")

        except exc.AuthLoginUserNotFound:
            return render_template("pages/auth_page/index.html",
                        error_message="Неверный логин или пароль!")

