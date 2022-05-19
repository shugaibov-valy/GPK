from views.auth_page import views


def install(app):
    app.add_url_rule(
        '/',
        view_func=views.AuthView.as_view('auth-page')
    )

