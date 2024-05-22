from flask import render_template
from flask_login import current_user

def regist():
    return render_template(
        "register.html", title = "registar usuario", current_user = current_user
    )
def loguear():
    return render_template(
        "login.html", title="inicio de sesion", current_user = current_user
    )
