#-------------------------------------------------------------------------------
# Name:        Login con BluePrint
# Purpose:     Sacarle nota a Daza dospuntos(w/2)
#
# Author:      Alguien
#
# Created:     19/09/1999
# Copyright:   (TM) ays 2021(?)
# Licence:     <uranus>
#-------------------------------------------------------------------------------

#importe de librerias
from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from flask_login import LoginManager, login_required, current_user, logout_user, login_user
from flask_sqlalchemy import SQLAlchemy

logbp = Blueprint('logbp', __name__, template_folder='templates')#

from app import db

#configuracion de ruta /login
@logbp.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')

#configuracion de ruta /signin
@logbp.route('/signin', methods=["GET", "POST"])
def signin():
    return render_template('signin.html')

#configuracion de ruta /forgotpass
@logbp.route('/forgotpass', methods=["GET", "POST"])
def forgotpass():
    return render_template('forgotpass.html')

#configuracion de ruta /logout
@logbp.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('logbp.login'))

def main():
    pass

if __name__ == '__main__':
    main()