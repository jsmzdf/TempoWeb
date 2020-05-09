
import threading
import time
class Temp:
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

    def iniciarCont(self, t: int):
        self.ingresarT(t)
        self.setBreak(True)

    def contar(self):
        self.setTAct(self.getTAct() - 1)

#############3 aqui comenza mi aventura $:

    def cont(self,ejer,num=0):
            seg=(num+1)%60
            if(seg<ejer)  :                      
                return [seg,'ejercicio']
            else:
                return [seg,'descanso']


#hilo para el codigode la app


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




ejercicio=30
parametro=2
t = threading.Thread(target=Temp.doit, args=(ejercicio,parametro,""))
t.start()
#estoesparamostrarquesedesactivathehilo para que vea que funcia puededarle menos tiempo
estoesparamostrarquesedesactivathehilo=parametro=120
time.sleep(estoesparamostrarquesedesactivathehilo)
t.do_run = False
t.join()





