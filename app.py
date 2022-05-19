
from flask import Flask
from views.auth_page import router as auth_router
from views.reg_page import router as reg_router
from views.main_page import router as main_router

def make_app() -> Flask:
    #proverka
    # Initialization the app application
    app = Flask(__name__)

    auth_router.install(app)
    reg_router.install(app)
    main_router.install(app)	
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return app
