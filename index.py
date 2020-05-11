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

app = Flask(__name__)

app.secret_key="dazanocalificadazanocalificadazasicalificasitienemonitorperodazanocalifica"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hoxwkmyfqupeab:c48a884b0095d4d7094b2543608cc2d10c58209a3370355bba9da6477a1c5f16@ec2-174-129-18-210.compute-1.amazonaws.com:5432/d1hi9b9fumoerc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
import GestionBD as gdb

#configuracion de ruta /
@app.route('/', methods=["GET", "POST"])
def index():
    return "<h1>Hola Al Mundo!</h1>"

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()