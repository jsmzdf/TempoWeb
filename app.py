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

#configuracion de ruta /
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
