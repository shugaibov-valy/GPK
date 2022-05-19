
#!/usr/bin/env python
from app import make_app


app = make_app()


# This function close the session
#@app.teardown_appcontext
#def shutdown_session(exception=None):
#    from db import session
#    session.remove()


# That "if" cycle starting server with debugging
if __name__ == "__main__":
    app.run()
