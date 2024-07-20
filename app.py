from flask import Flask, Blueprint, redirect, render_template, request, url_for
import os
from dotenv import load_dotenv

# Conexion a Base de datos
from db import db

# controladores
from controllers.home_controller import home

# cargar datos de variables de entorno
load_dotenv()


# inicializacion del app Flask y demas componentes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializo ORM SQLAlchemy
db.init_app(app)

with app.app_context():
    db.create_all()

# registro de los diferentes controladores en app
app.register_blueprint(home)
    
if __name__ == '__main__':
    app.run(debug=True)