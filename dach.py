#####################################################################
#                                                                   #
#                   Copyright(c) 2018                               #
#       Dariusz Nowakowski  <bozondn AT gmail DOT com>              #
#                                                                   #
#####################################################################

import RPi.GPIO as GPIO
import os
import time


def roof():
	GPIO.output(lista, 0)
	time.sleep(2)

	stan1 = GPIO.input(22)     # PIN number
	stan2 = GPIO.input(23)     # PIN number

	if stan1 == 0 and stan2 == 0:
		GPIO.output(27, 0)
		print 'Zamykam dach...'
		time.sleep(20)

	GPIO.output(27, 1)
	time.sleep(2)
	print 'Dach zamkniety'

while True:
	GPIO.setmode(GPIO.BCM)
	lista = (22, 23)  
	dePos = os.popen('indi_getprop -1 -h 192.168.1.10 -p 7624 "EQMod Mount.CURRENTSTEPPERS.DEStepsCurrent"')
	pos1 = dePos.read()
	s = pos1
	parkDE = s.strip()
	DE = "7504887" 
	
	raPos = os.popen('indi_getprop -1 -h 192.168.1.10 -p 7624 "EQMod Mount.CURRENTSTEPPERS.RAStepsCurrent"')
	pos2 = raPos.read()
	s = pos2
	parkRA = s.strip()
	RA = "10530800"
	
	if DE == parkDE and RA == parkRA:
		GPIO.setup(lista, GPIO.OUT)
		GPIO.setup(27, GPIO.OUT)
		roof()
		GPIO.cleanup()
		break
	else:
		print "Montaz nie zaparkowany"
	time.sleep(600)
