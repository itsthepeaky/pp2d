# pt motor cu fir albastru:       IN1-  11         IN2-  8


import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


#motor dreapta spate
gpio.setup(11, gpio.OUT)
gpio.setup(8, gpio.OUT)
gpio.setup(12, gpio.OUT)
pwm_dreapta=gpio.PWM(12,100)
 


gpio.setup(20, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(13, gpio.OUT)
pwm_stanga=gpio.PWM(13,100)




def roti_dreapta_backward():

	gpio.output(11,False)
	gpio.output(8,True)

	


def roti_dreapta_stop():

	gpio.output(11,False)
	gpio.output(8,False)




def roti_stanga_backward():

	gpio.output(26,False)
	gpio.output(20,True)

	


def roti_stanga_stop():

	gpio.output(26,False)
	gpio.output(20,False)




def roti_dreapta_forward():

	gpio.output(8,False)
	gpio.output(11,True)

	


def roti_stanga_forward():

	gpio.output(20,False)
	gpio.output(26,True)

	











def roti_backward():
	roti_stanga_backward()
	roti_dreapta_backward()

def roti_stop():
	roti_stanga_stop()
	roti_dreapta_stop()

def roti_forward():
	roti_stanga_forward()
	roti_dreapta_forward()


def roti_curba_dreapta():
	
	roti_stanga_forward()
	roti_dreapta_forward()
	pwm_stanga.start(100)
	pwm_dreapta.start(25)
	time.sleep(5)

def roti_curba_stanga():
    
    roti_stanga_forward()
    roti_dreapta_forward()
    pwm_stanga.start(25)
    pwm_dreapta.start(100)
    time.sleep(5)

def roti_fata_all():
    roti_stanga_forward()
    roti_dreapta_forward()
    pwm_stanga.start(100)
    pwm_dreapta.start(100)
    time.sleep(5)

def roti_spate_all():
    roti_stanga_backward()
    roti_dreapta_backward()
    pwm_stanga.start(100)
    pwm_dreapta.start(100)
    time.sleep(5)


#roti_curba_dreapta()
#roti_stop()
#roti_curba_stanga()
#roti_stop()
#roti_fata_all()
#roti_stop()
#roti_spate_all()
#roti_stop()






























