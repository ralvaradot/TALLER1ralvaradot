from flask import Blueprint, render_template, request
from models.usuario import Usuario
from db  import db

home = Blueprint('home', __name__)

@home.route('/')
def index():
    usuarios = Usuario.query.all()
    
    return render_template('base.html')

@home.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        
        #user = Usuario('','',0)
        try:
            #user = db.session.execute(db.select(Usuario).filter_by(username=username, password=password)).first()
  
            user = Usuario.query.filter_by(username=username, password=password).first()    
            if user != None:
                if user.is_admin == 1:
                    usuarios = Usuario.query.all()
                    return render_template('administrador.html', usuarios=usuarios)
                else:
                    return render_template('usuario.html',user=user)
            else:
                return render_template('usuario_invalido.html')
        except:   
            return render_template('usuario_invalido.html')
