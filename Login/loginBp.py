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
from App import db

laaa = 1
logbp = Blueprint('logbp', __name__, template_folder='templates')#

#configuracion de ruta /login
@logbp.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')

def main():
    pass

if __name__ == '__main__':
    main()