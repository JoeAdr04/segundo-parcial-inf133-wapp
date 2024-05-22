from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_doctor, logout_doctor, login_required, current_doctor
from werkzeug.security import check_password_hash
from utils.decorators import role_required
from views import doctor_view
from models.doctor_model import Doctor

doctor_bp = Blueprint("user", __name__)

@doctor_bp.route("/")
def index():
    return redirect(url_for("doctor.login"))

@doctor_bp.route("/doctors", methods=["GET", "POST"])
def create_doctor():
    if request.method == "POST":
        doctorname = request.form["doctorname"]
        password = request.form["password"]
        role = request.form["role"]
        existing_doctor = Doctor.query.filter_by(doctorname=doctorname).first()
        if existing_doctor:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("doctor.create_doctor"))
        doctor = Doctor(doctorname, password, role)
        doctor.set_pass(password)
        doctor.save()
        flash("usuario creado con exito", "succes")
        return redirect(url_for("doctor.index"))
    return redirect(url_for("doctor.index"))

@doctor_bp.route("/login", methods=["GET", "POST"])
def login_doctor():
    if request.method == "POST":
        doctorname = request.form["doctorname"]
        password = request.form["password"]
        doctor = Doctor.get_doctor_by_doctorname(doctorname)
        if doctor and check_password_hash(doctor.password_hash, password):
            login_doctor(doctor)
            flash("Inicio de sesión exitoso", "success")
        else:
            flash("Nombre de usuario o contraseña incorrectos", "error")
    return doctor_view.loguear()

@doctor_bp.route("/logout")
@login_required
def logout():
    logout_doctor()
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("doctor.login"))