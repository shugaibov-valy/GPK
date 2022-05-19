from views.reg_page import views


def install(app):
    app.add_url_rule(
        '/reg',
        view_func=views.RegView.as_view('reg-page')
    )

