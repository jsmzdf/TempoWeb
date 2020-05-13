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

logbp = Blueprint('logbp', __name__, template_folder='templates')#

from app import db
import ModelosBD as mdb
@logbp.route('/login', methods=["GET", "POST"])
@login_required
def login():
    if 'mess' not in session:
        session['mess']={}
    if current_user.is_authenticated:
        return redirect(url_for('Rutina'))
    if "usuario_temp" in session:
        session["usuario_temp"] = {}
    if (request.method=="GET"):
        return render_template('login.html')
    else:
        try:
            usu = request.form['nmUserLog']
            passuslg = request.form['psUserLog']
        except:
            #session['mess']['alertas'].append("Fallo en el envio de datos. Revise los campos.")
            flash("Fallo en el envio de datos. Revise los campos.")
            return redirect(url_for('login'))
        #passlg_encode = passlg.encode("utf-8")

        try:
            userFnd = mdb.usuario.query.filter_by(nom_usu=usu).first()
        except:
            #session['mess']['alertas'].append("Usuario no encontrado. Revise el campo de email.")
            flash("Usuario no encontrado.")
            return redirect(url_for('login'))

        if userFnd!=None:
            if userFnd.contra_usu == passuslg:
                login_user(userFnd)
                return redirect(url_for('login'))
            else:
                #session['mess']['alertas'].append("Contraseña incorrecta. Revise el campo de contraseña.")
                flash("Contraseña incorrecta. Revise el campo de contraseña.")
                return redirect(url_for('login'))
        else:
            #session['mess']['alertas'].append("Usuario no encontrado. Revise el campo de email.")
            flash("Usuario no encontrado.")
            return redirect(url_for('login'))

@logbp.route('/signin', methods=["GET", "POST"])
@login_required
def signin():
    if 'mess' not in session:
        session['mess']={}
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    if (request.method=="GET"):
        if "usuario_temp" in session:
            for dat in ["name","last"]:
                if dat not in session["usuario_temp"]: session["usuario_temp"][dat]=""
            if "imag" not in session["usuario_temp"]:
                session["usuario_temp"]["imag"]="http://adoracionysanidad.herokuapp.com/static/recourses/icon-user.png"
        else:
            session["usuario_temp"]={}
            session["usuario_temp"]["name"] = ""
            session["usuario_temp"]["last"] = ""

        return render_template('signin.html')
    else:
        allright = True
        scopes = ["name","last"]
        spaces = ['userNom', 'userApe']
        signif = ['nombre', 'apellido']
        for dat in range(len(scopes)):
            if spaces[dat] in request.form and request.form[spaces[dat]] != "": session["usuario_temp"][scopes[dat]]=request.form[spaces[dat]]
            else:
                allright = False
                flash("Revise el campo de %s" % signif[dat])
        scopes = ["prof","alma"]
        spaces = ['userPrf', 'userUni']
        for dat in range(len(scopes)):
            if spaces[dat] in request.form: session["usuario_temp"][scopes[dat]]=request.form[spaces[dat]]
        if 'correo' in request.form:
            usMail = request.form['correo']
            if db.search('', usMail) is None:
                allright = False
                flash("Revise el campo de email, no es un formato correcto")
            else:
                session["usuario_temp"]["mail"] = usMail
        if 'usu' in request.form:
            usPhon = request.form['usu']
            if db.search('', usPhon) is None:
                allright = False
                flash("Revise el campo de ususario, no es un formato correcto")
            else:
                session["usuario_temp"]["phon"] = usPhon

        else:
            flash("Ya existe ese email de usuario, prueba en iniciar sesion")
        return redirect(url_for('login'))

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