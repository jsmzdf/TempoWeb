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
import App

app = Flask(__name__)

app.secret_key = App.SK

app.config['SQLALCHEMY_DATABASE_URI'] = App.URI
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