# TempoWeb


### Juan Sebastian Mancera Gaitán 20171020047
### John Sebastian Martinez Zabala 20171020059
### Pedro Enrique Barrera 20171020057

Aplicación Every Minute On the Minute y manejo de usuarios pensado en componentes para el reuso.

Componentes para el reuso:

-Login:El módulo Login se pensó como un blueprint en el framework Flask para permitir su reutilización en cualquier otra plantilla Flask solo siendo necesario registrar el blueprint de nuevo.

-Temporalizador:  

Cuando el objeto Temporalizador se actualiza se le puede ingresar una función de un unico parámetro  la cual es la encargada de actualizar  el tiempo, es decir cualquier función cuyo objetivo sea relacionada con contabilizar el tiempo de acuerdo a distintos aspectos y reciba un único parámetro puede utilizar el temporalizador de manera dinámica. 

Esto se aplico de la siguiente manera: 

En la clase Rutina el objeto temporalizar se puede utilizar de tres maneras diferentes para tres funciones diferentes de salida.
