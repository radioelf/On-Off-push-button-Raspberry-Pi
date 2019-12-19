#!/usr/bin/env python

"""
Parar 
sudo /etc/init.d/listen-for-shutdown.sh stop
Arrancar
sudo /etc/init.d/listen-for-shutdown.sh start
pin BCM 3 pulsador On/OFF
pin BCM 21 Led estado
"""
# Importamos los modulos para enviar comandos al sistema
from subprocess import call
# Importamos acceso a pines de la Raspberry
import RPi.GPIO as GPIO
# Importamos gestion de tiempo
import time

#Definimos la funcion de apagado
def apagar():                  		          							# Invertimos estado OnOff
	OnOff = True
	while 1:
		GPIO.wait_for_edge(3, GPIO.FALLING, timeout=1000) 				# Esperamos cambio de estado en pin 3 o 1 segundo
		if GPIO.input(3):                                       		# Si NO se esta pulsando
			GPIO.output(21, OnOff)                          			# Parpadeo led RUN...
            OnOff = not OnOff
        else:
			Ciclos =0
			while Ciclos < 30 and GPIO.input(3) == False:   			# Esperamos si tenemos menos de 3 segundos pulsacion en pin 3
				Ciclos =Ciclos +1
				OnOff = not OnOff
                                GPIO.output(21, OnOff)
				time.sleep(0.1)											# Espera de 100ms
			if Ciclos > 29:
				GPIO.output(21, False) 
				call(['shutdown', '-h', 'now'], shell=False) 			# Ejecutar el comando de apagar
# Inicio
if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)            									# Modo numeracion pines BCM
	GPIO.setwarnings(False)
	GPIO.setup(21, GPIO.OUT)          									# Pin 21 como salida LED
	GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) 					# Pin 3 como entrada y pull-up
	GPIO.output(21, True)              									# Encendemos led
	apagar()  															# Llamamos a la funcion de apagar al iniciar
