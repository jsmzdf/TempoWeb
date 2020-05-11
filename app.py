<<<<<<< HEAD

from flask import Flask, render_template, request
import pandas as pd
import numpy as np



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9090, debug=True)
=======
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

'''en este lugar ponemos variables y constantes'''
URI = 'postgres://hoxwkmyfqupeab:c48a884b0095d4d7094b2543608cc2d10c58209a3370355bba9da6477a1c5f16@ec2-174-129-18-210.compute-1.amazonaws.com:5432/d1hi9b9fumoerc'
SK = 'loquetenemosaquiesclaramenteungalimatiasunafanfarreachacharatescaycalifrajilistica'
>>>>>>> d25155b59832eb43ba625531de6669ce41843881
