from db import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    is_admin = db.Column(db.Integer, nullable=False)
    
    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin