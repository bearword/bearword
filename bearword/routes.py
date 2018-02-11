from flask import redirect, render_template
from flask_login import UserMixin, login_user, logout_user

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
    def get_name(self):
        return "Paul Dirac"

def setup_auth(app, login_manager, blog_engine):
    @login_manager.user_loader
    @blog_engine.user_loader
    def load_user(user_id):
        return User(user_id)

    @app.route("/login/")
    def login():
        login_user(User("pdirac"))
        return redirect("/blog")

    @app.route("/logout/")
    def logout():
        logout_user()
        return redirect("/")
    return app
