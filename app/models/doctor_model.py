from database import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Doctor(UserMixin, db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable = False)
    password_hash = db.Column(db.String(128), unique=True,nullable = False)
    role = db.Column(db.String(50), nullable = False)

    
    def set_pass(self, password):
        self.password_hash = generate_password_hash(password)

    def __init__(self, username, password, role):
        self.username = username
        self.set_pass(password)
        self.role = role

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Doctor.query.all()
    
    @staticmethod
    def get_id(id):
        return Doctor.query.get(id)
    
    def update():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def has_role(self, role):
        return self.role == role
    @staticmethod
    def get_user_by_username(username):
        return Doctor.query.filter_by(username=username).first()