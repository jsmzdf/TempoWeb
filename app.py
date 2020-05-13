#-------------------------------------------------------------------------------
# Name:        Modulo Algo
# Purpose:     Sacarle nota a Daza dospuntos(w/2)
#
# Author:      Alguien
#
# Created:     19/09/1999
# Copyright:   (TM) ays 2021(?)
# Licence:     <uranus>
#-------------------------------------------------------------------------------

#importe de librerias
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_login import LoginManager, login_required, current_user, logout_user, login_user
from flask_sqlalchemy import SQLAlchemy
import index
from datetime import datetime

app = Flask(__name__)

app.secret_key = index.SK

app.config['SQLALCHEMY_DATABASE_URI'] = index.URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

from Login.loginBp import logbp
# register our blueprints
app.register_blueprint(logbp)

import ModelosBD as mdb

#inicializacion el logeo
login_manager = LoginManager(app)
login_manager.login_view = 'logbp.login'

@login_manager.user_loader
def load_user(user_id):
    return mdb.usuario.query.get(int(user_id))

#configuracion de ruta /
@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    #rutina = mdb.rutina.query.all()
    rutinas = list(current_user.realizo)
    return render_template('index.html', rutinas=rutinas)

#configuracion de ruta /sesion
@app.route('/sesion', methods=["GET", "POST"])
@login_required
def sesion():
    #ayuda para Savital
    #rut = mdb.rutina("Pierna", '2020-4-1 9:46', 30, 30, 20, 20, objusuario.id_usu) #esto va si quiere hacerlo con una fecha y usuario especificos
    #rut = mdb.rutina("Pierna", '2020-4-1 9:46', 30, 30, 20, 20, current_user.id_usu) #esto va si quiere hacerlo con el usuario logeado actual
    #rut = mdb.rutina("Brazo", datetime.utcnow(), 30, 30, 120, 600, current_user.id_usu) #esto va si quiere hacerlo con la fecha actual
    #db.session.add(rut)
    #db.session.commit()
    return redirect(url_for('index'))

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
