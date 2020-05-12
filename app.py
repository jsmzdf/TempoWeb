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
    user = mdb.usuario.query.filter_by(nom_usu="1111111").first()
    login_user(user)

    #obj = mdb.rutina("pierna", '2020-4-1 9:46', 30, 30, 20, 20)
    #db.session.add(obj)
    #db.session.commit()
    rutina = mdb.rutina.query.all()
    rut=[rutina[x].nom_rut for x in range(len(rutina))]
    print(rut)
    return render_template('index.html', rutina=rut)

#configuracion de ruta /callback
@app.route('/callback', methods=["GET", "POST"])
def callback():
    user = mdb.usuario.query.filter_by(nom_usu="1111111").first()
    login_user(user)

    obj = mdb.rutina("pierna", '2020-4-1 9:46', 30, 30, 20, 20)
    db.session.add(obj)
    db.session.commit()
    rutina = mdb.rutina.query.all()

    return redirect(url_for('index', rutina=rutina))


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
