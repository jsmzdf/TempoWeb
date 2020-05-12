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

class Intervalo:
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

    def detener(self):
        self.ejrc.detener()
        self.dscn.detener()
        self.rutn.detener()
        self.brkr = False

    def controladorState(self, tAct):
        print("Quedan", tAct, "segundos de ", self.stat)
        if tAct == 0:
            if self.stat == "Ejercicio":
                self.ejrc.detener()
                self.stat = "Descanso"
            elif self.stat == "Descanso":
                self.dscn.detener()
                self.stat = "Ejercicio"
            if self.brkr == True:
                self.iniciarState()

    def iniciarState(self):
        if self.stat == "Ejercicio":
            self.ejrc.iniciar(self.ejrc.getTReal(), salida=self.controladorState)
        elif self.stat == "Descanso":
            self.dscn.iniciar(self.dscn.getTReal(), salida=self.controladorState)

    def controlarRutina(self, tAct):
        print("Quedan", tAct, "segundos de la rutina total de", self.nomb)
        if tAct == 0:
            self.detener()
            print("La rutina", self.nomb, "ha finalizado totalmente")

    def iniciar(self):
        self.brkr = True
        self.rutn.iniciar(self.rutn.getTReal(), salida=self.controlarRutina)
        self.iniciarState()

    def getBreak(self):
        return self.brkr



def main():
    r = Rutina("Pierna", 30, 5, 10)
    r.iniciar()
    while r.getBreak():
        continue

if __name__ == '__main__':
    main()
