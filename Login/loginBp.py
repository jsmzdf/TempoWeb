#-------------------------------------------------------------------------------
# Name:        tengo hambre
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

logbp = Blueprint('logbp', __name__, template_folder='templates', static_folder='static', static_url_path='/Login/static')#

try: from App import db
except: from app import db
import ModelosBD as mdb

@logbp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if (request.method=="GET"):
        return render_template('login.html')
    else:
        try:
            usu = request.form['nmUserLog']
            passuslg = request.form['psUserLog']
        except:
            flash("Fallo en el envio de datos. Revise todos los campos.")
            return redirect(url_for('logbp.login'))
        #passlg_encode = passlg.encode("utf-8")

        try:
            userFnd = mdb.usuario.query.filter_by(nom_usu=usu).first()
        except:
            flash("Usuario no encontrado.")
            return redirect(url_for('logbp.login'))

        if userFnd != None:
            if userFnd.contra_usu == passuslg:
                login_user(userFnd)
                return redirect(url_for('logbp.login'))
            else:
                flash("Contraseña incorrecta. Revise el campo de contraseña.")
                return redirect(url_for('logbp.login'))
        else:
            flash("Usuario no encontrado.")
            return redirect(url_for('logbp.login'))

@logbp.route('/signin', methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('logbp.login'))
    if (request.method=="GET"):
        return render_template('signin.html')
    else:
        try:
            usu = request.form['nmUserLog']
            passuslg = request.form['psUserLog']
        except:
            flash("Fallo en el envio de datos. Revise todos los campos.")
            return redirect(url_for('logbp.signin'))

        user = mdb.usuario(usu, passuslg)

        try:
            userFnd = mdb.usuario.query.filter_by(nom_usu=usu).first()
        except: pass

        if userFnd == None:
            try:
                db.session.add(user)
                db.session.commit()
                login_user(user)
            except:
                flash("Fallo en el envio de datos. Revise todos los campos. El nombre de usuario debe utilizar unicamente letras de A-z y numeros de 0-9")
                return redirect(url_for('logbp.signin'))
        else:
            flash("Ya existe ese usuario, prueba en iniciar sesion")
        return redirect(url_for('logbp.login'))

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