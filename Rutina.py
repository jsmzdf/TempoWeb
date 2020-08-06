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

class Rutina:
    def __init__(self, nomb: str, tRutn: int, foutRut: callable,
        tDesc: int, foutDesc: callable, tEjer: int, foutEjer: callable):
        self.nomb = nomb
        self.rutn = Temporalizador()
        self.rutn.ingresarT(tRutn)
        self.foutRutn = foutRut
        self.ejrc = Temporalizador()
        self.ejrc.ingresarT(tEjer)
        self.foutEjrc = foutEjer
        self.dscn = Temporalizador()
        self.dscn.ingresarT(tDesc)
        self.foutDscn = foutDesc
        self.brkr = False
        self.stat = "Ejercicio"

    def detener(self):
        self.ejrc.detener()
        self.dscn.detener()
        self.rutn.detener()
        self.brkr = False

    def cambiarStado(self):
        if self.stat == "Ejercicio":
            self.stat = "Descanso"
        elif self.stat == "Descanso":
            self.stat = "Ejercicio"

    def controladorState(self, tAct):
        print("Quedan", tAct, "segundos de ", self.stat)
        if self.stat == "Ejercicio" and self.foutEjrc:
            self.foutEjrc(tAct)

        if self.stat == "Descanso" and self.foutDscn:
            self.foutDscn(tAct)

        if int(tAct) == 0:
            if self.stat == "Ejercicio":
                self.ejrc.detener()
            elif self.stat == "Descanso":
                self.dscn.detener()
            self.cambiarStado()

            if self.brkr == True:
                self.iniciarState()

    def iniciarState(self):
        if self.stat == "Ejercicio":
            self.ejrc.iniciar(self.ejrc.getTReal(), salida=self.controladorState)
        elif self.stat == "Descanso":
            self.dscn.iniciar(self.dscn.getTReal(), salida=self.controladorState)

    def controlarRutina(self, tAct):
        print("Quedan", tAct, "segundos de la rutina total de", self.nomb)
        if self.foutRutn:
            self.foutRutn(tAct)

        if int(tAct) == 0:
            self.detener()
            print("La rutina", self.nomb, "ha finalizado totalmente")

    def iniciar(self):
        self.brkr = True
        self.rutn.iniciar(self.rutn.getTReal(), salida=self.controlarRutina)
        self.iniciarState()

    def getBreak(self):
        return self.brkr

def main():
    r = Rutina("Pierna", 15.0, None, 5.0, print, 10.0, None)
    r.iniciar()
    while r.getBreak():
        continue

if __name__ == '__main__':
    main()
