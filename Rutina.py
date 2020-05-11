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
import Temporalizador

class descanso:
    pass

class ejercicio:
    pass

class Rutina:
    pass

def main():
    t = Temporizador()
    t.iniciar(5)
    while t.getBreak():
        continue

if __name__ == '__main__':
    main()
