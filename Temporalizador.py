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
import time

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
        self.contar()

    def contar(self):
        if self.getTAct() > 0:
            threading.Timer(1,lambda: [self.setTAct(self.getTAct() - 1),print(self.getTAct()), self.contar()]).start()
        else:
            self.detener()

    def cont(self,ejer,num=0):
        seg=(num+1)%60
        if(seg<ejer)  :
            return [seg,'ejercicio']
        else:
            return [seg,'descanso']

    def doit(self,ejer,tiempo,arg):
        i=0
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            for i in range(60):
                time.sleep(1)
                msg=str(Temp.cont(ejer,i) )
                print(msg+" minutos:"+str(1))
            i=i+1
            if(i==tiempo):
                return[0,0]                         #t._wait_for_tstate_lock() pausa el hilo
        return[0,0]

def main():
    t = Temporizador()
    t.iniciar(5)
    while t.getBreak():
        continue
    '''
    ejercicio=30
    parametro=2
    t = threading.Thread(target=Temp.doit, args=(ejercicio,parametro,""))
    t.start()
    #estoesparamostrarquesedesactivathehilo para que vea que funcia puededarle menos tiempo
    estoesparamostrarquesedesactivathehilo=parametro=120
    time.sleep(estoesparamostrarquesedesactivathehilo)
    t.do_run = False
    t.join()'''

if __name__ == '__main__':
    main()





