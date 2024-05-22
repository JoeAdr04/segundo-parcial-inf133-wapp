from flask import Flask
from flask_login import LoginManager


from controllers import doctor_controller

from controllers import patient_controller

from database import db
from models.doctor_model import Doctor

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pacientes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"

login_manager = LoginManager()

login_manager.login_view = "doctor.loguear"
login_manager.init_app(app)


# Función para cargar un usuario basado en su ID
@login_manager.user_loader
def load_user(user_id):
    return Doctor.query.get(int(user_id))


# Inicializa `db` con la aplicación Flask
db.init_app(app)
# Registra el Blueprint de usuarios
app.register_blueprint(doctor_controller.doctor_bp)
app.register_blueprint(patient_controller.patient_bp)

if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
