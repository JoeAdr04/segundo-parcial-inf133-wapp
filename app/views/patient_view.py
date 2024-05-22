from flask import render_template

from flask_login import current_user

def list_patient(patients):
    return render_template(
        "patients.html", patients = patients, title = "listar a todos los pacientes", current_user = current_user,
    )

def create_patient():
    render_template(
        "create_patients.html", title= "crear un paciente", current_user = current_user
    )

def update_patient(patient):
    render_template(
        "update_patient.html", patient = patient, title = "actualizar paciente", current_user = current_user
    )

