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
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_required, current_user, logout_user, login_user
from flask_sqlalchemy import SQLAlchemy
import index
from datetime import datetime
#from functools import partial
import Rutina as rt

app = Flask(__name__)

app.config['SECRET_KEY'] = index.SK

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

def sesssETTot(tAct: float):
    fkSession["tAct"] = tAct

def sesssETEjr(tAct: float):
    fkSession["tEje"] = tAct

def sesssETDsc(tAct: float):
    fkSession["tDes"] = tAct

fkSession = {'tAct': 0, 'tDes': 0, 'tEje': 0}

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
    print("Va por ", request.method)
    if (request.method=="GET"):
        return render_template('rutina.html', tiempos = fkSession)
    else:
        try:
            newRut = request.form['nomRut']
            nomRut = request.form['nomRutPre']
            mins = request.form['tMinT']
            segs = request.form['tSegT']
            ejrs = request.form['tSegE']
        except:
            flash("Fallo en el envio de datos. Revise los campos.")
            return redirect(url_for('index'))

        if nomRut == "Otra":nomRut = newRut

        for dats in [mins, segs, ejrs]:
            if dats == "":dats= 0

            try:
                dats = float(dats)
            except:
                flash("Fallo en el envio de datos. Algun campo numerico no es valido.")
                return redirect(url_for('index'))

        if nomRut == "" or not nomRut:
            flash("Nombre de rutina erroneo.")
            return redirect(url_for('index'))

        #rut = rt.Rutina(nomRut, float(float(mins)*60)+float(segs), sesssETTot, float(60-float(ejrs)), sesssETDsc, float(ejrs), sesssETEjr)
        fkSession['rNom'] = str(nomRut)
        fkSession['tAct'] = int(float(float(mins)*60)+float(segs))
        fkSession['tDes'] = int(60-float(ejrs))
        fkSession['tEje'] = int(ejrs)
        #ayuda para Savital
        #rut = mdb.rutina("Pierna", '2020-4-1 9:46', 30, 30, 20, 20, objusuario.id_usu) #esto va si quiere hacerlo con una fecha y usuario especificos
        #rut = mdb.rutina("Pierna", '2020-4-1 9:46', 30, 30, 20, 20, current_user.id_usu) #esto va si quiere hacerlo con el usuario logeado actual
        #rut = mdb.rutina("Brazo", datetime.utcnow(), 30, 30, 120, 600, current_user.id_usu) #esto va si quiere hacerlo con la fecha actual
        #db.session.add(rut)
        #db.session.commit()
        return render_template('rutina.html', tiempos = fkSession)

#configuracion de ruta /callback
@app.route('/callback', methods=["GET", "POST"])
@login_required
def callback():
    #rutina = mdb.rutina.query.all()
    #return redirect(url_for('index'))
    return str(fkSession)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
