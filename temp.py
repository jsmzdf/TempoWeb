# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:48:54 2020

@author: (╯°□°)╯︵ ┻━┻
"""

import threading
import time

def cont(ejer,num=0):
        seg=(num+1)%60
        if(seg<ejer)  :                      
            return [seg,'ejercicio']
        else:
            return [seg,'descanso']


#hilo para el codigode la app
        
def doit(ejer,tiempo,arg):
    i=0
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        
        for i in range(60):
                    time.sleep(1)            
                    msg=str(cont(ejer,i) )
                    print(msg+" minutos:"+str(1))
        i=i+1
        if(i==tiempo):
            return[0,0]                         #t._wait_for_tstate_lock() pausa el hilo
    return[0,0]

ejercicio=30
parametro=2
t = threading.Thread(target=doit, args=(ejercicio,parametro,""))
t.start()
#estoesparamostrarquesedesactivathehilo para que vea que funcia puededarle menos tiempo
estoesparamostrarquesedesactivathehilo=parametro=120
time.sleep(estoesparamostrarquesedesactivathehilo)
t.do_run = False
t.join()


