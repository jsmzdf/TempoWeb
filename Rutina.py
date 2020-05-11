#-------------------------------------------------------------------------------
# Name:        Rutina
# Purpose:     Sacarle nota a Daza 2(.(w/4))
#
# Author:      Alg&uacute;n Qui&eactute;n
#
# Created:     19/09/1999
# Copyright:   (TM) JSM y PB 2021(?)
# Licence:     <uranus>
#-------------------------------------------------------------------------------

#importe de librerias
from Temporalizador import *

class intervalo:
    def __init__(self, tInt: int):
        self.temp = Temporalizador()
        self.temp.iniciar(tInt)

    def iniciar(self):
        pass

class Rutina:
    def __init__(self, nomb: str, tRutn: int,
        tDesc: int, tEjer: int):
        self.nomb = nomb
        self.rutn = Temporalizador()
        self.rutn.ingresarT(tRutn)
        self.ejrc = Temporalizador()
        self.ejrc.ingresarT(tEjer)
        self.dscn = Temporalizador()
        self.dscn.ingresarT(tDesc)
        self.brkr = False
        self.stat = "Ejercicio"

    def controladorState(self, tAct):
        print(self.stat, tAct)
        if tAct == 0:
            if self.stat == "Ejercicio":
                self.stat = "Descanso"
            elif self.stat == "Descanso":
                self.stat = "Ejercicio"
            self.iniciarState()

    def iniciarState(self):
        if self.stat == "Ejercicio":
            self.ejrc.iniciar(self.ejrc.getTReal(), salida=self.controladorState)
        elif self.stat == "Descanso":
            self.dscn.iniciar(self.dscn.getTReal(), salida=self.controladorState)

    def iniciar(self):
        self.brkr = True
        self.rutn.iniciar(self.rutn.getTReal())
        self.iniciarState()

    def getBreak(self):
        return self.brkr

def main():
    r = Rutina("Pierna", 60, 5, 10)
    r.iniciar()
    while r.getBreak():
        continue

if __name__ == '__main__':
    main()
