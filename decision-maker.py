#!/usr/bin/env python
# coding: latin-1
# Ingmar Stapel
# Date: 20170615
# Version Alpha 0.1
# Decision Maker

from time import sleep
import RPi.GPIO as GPIO
import os
#from random import randint
import random

GPIO.setmode(GPIO.BCM)

# Verwendete Pins des ULN2003A auf die Pins des Rapberry Pi
# zugeordnet 
IN1=6 # IN1
IN2=13 # IN2
IN3=19 # IN3
IN4=26 # IN4

# Wartezeit regelt die Geschwindigkeit wie schnell sich der Motor
# dreht.
time = 0.001

# Pins aus Ausgänge definieren
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
# Alle Pins werden initial auf False gesetzt. So dreht sich der 
# Stepper-Motor nicht sofort irgendwie.
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# Der Schrittmotoren 28BYJ-48 ist so aufgebaut, das der Motor im
# Inneren 8 Schritte für eine Umdrehung benötigt. Durch die Betriebe
# benätigt es aber 512 x 8 Schritte damit die Achse sich einmal um
# sich selbt also 360° dreht.

# Definition der Schritte 1 - 8 über die Pins IN1 bis IN4
# Zwischen jeder Bewegung des Motors wird kurz gewartet damit der
# Motoranker seine Position erreicht.
def Step1():
    GPIO.output(IN4, True)
    sleep (time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

# Umdrehung links herum  
def left(step):	
	for i in range (step):   
		#os.system('clear') # verlangsamt die Bewegung des Motors zu sehr. 
		Step1()
		Step2()
		Step3()
		Step4()
		Step5()
		Step6()
		Step7()
		Step8()  
		print "Step left: ",i

# Umdrehung rechts herum		
def right(step):
	for i in range (step):
		#os.system('clear') # verlangsamt die Bewegung des Motors zu sehr.  
		Step8()
		Step7()
		Step6()
		Step5()
		Step4()
		Step3()
		Step2()
		Step1()  
		print "Step right: ",i	
		
# Hier faellt die Entscheidung ob links oder rechts herum
if random.randint(0, 2) >= 1:
	# Hier wird ermittelt wie weit sich der Motor dreht.
	left(random.randint(100, 1024))
else:
	# Hier wird ermittelt wie weit sich der Motor dreht.
	right(random.randint(100, 1024))
GPIO.cleanup()
