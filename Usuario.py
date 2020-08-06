#-------------------------------------------------------------------------------
# Name:        Usuario
# Purpose:     Sacarle nota a Daza 2(.(w/4))
#
# Author:      Alg&uacute;n Qui&eactute;n
#
# Created:     19/09/1999
# Copyright:   (TM) JSM y PB 2021(?)
# Licence:     <uranus>
#-------------------------------------------------------------------------------

#importe de librerias

class Usuario:
    def __init__(self, nombre, rutina):
        self.__nombre = nombre
        self.__rutina = rutina

    def getnombre(self):
        return self.__nombre

    def getrutina(self):
        return self.__rutina

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setrutina(self, rutina):
        self.__rutina = rutina

    def delnombre(self):
        del self.__nombre

    def delrutina(self):
        del self.__rutina

