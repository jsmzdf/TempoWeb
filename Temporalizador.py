#-------------------------------------------------------------------------------
# Name:        Temporalizador
# Purpose:     Sacarle nota a Daza 2(.(w/4))
#
# Author:      Alg&uacute;n Qui&eactute;n
#
# Created:     19/09/1999
# Copyright:   (TM) JSM y PB 2021(?)
# Licence:     <uranus>
#-------------------------------------------------------------------------------

#importe de librerias
import threading

class Temporizador:
    def __init__(self):
        '''inicializa el Temporalizador con 0 segundos y pausado'''
        self.tReal = 0
        self.tAct = 0
        self.breaker = False

    def setTReal(self, t: int):
        self.tReal = t

    def setTAct(self, t: int):
        self.tAct = t

    def setBreak(self, b: bool):
        self.breaker = b

    def getTReal(self) -> int:
        return self.tReal

    def getTAct(self) -> int:
        return self.tAct

    def getBreak(self) -> bool:
        return self.breaker

    def reset(self):
        self.ingresarT(self.tReal)

    def ingresarT(self, t: int):
        self.setTReal(t)
        self.setTAct(t)

    def detener(self):
        self.setBreak(False)

    def continuar(self):
        self.setBreak(True)

    def iniciar(self, t: int, salida = None):
        self.ingresarT(t)
        self.setBreak(True)
        self.contar(salida = salida)

    def contar(self, salida = None):
        if self.getTAct() > 0:
            threading.Timer(1,lambda: [self.setTAct(self.getTAct() - 1),print(self.getTAct()), salida, self.contar(salida=salida)]).start()
        else:
            self.detener()

def main():
    t = Temporizador()
    t.iniciar(5, salida=lambda:[print(t.getTAct())])
    while t.getBreak():
        continue

if __name__ == '__main__':
    main()





