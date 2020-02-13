#Hasan Alameh's PiCart

#Import time & GPIO controller modules
import time
import RPi.GPIO as GP

#Using BroadCom channels for pin referencing
GP.setmode(GP.BCM)

#Disable any warnings script
GP.setwarnings(False)

#Set mode of used pins as output
GP.setup(18,GP.OUT)
GP.setup(22,GP.OUT)
GP.setup(17,GP.OUT)
GP.setup(23,GP.OUT)

#Move forward 1.5 seconds
GP.setup(17,True)
GP.setup(18,False)
GP.setup(22,True)
GP.setup(23,False)
time.sleep(1.5)

#Turn left for approx 1 second
GPIO.setup(17,True)
GPIO.setup(18,False)
GPIO.setup(22,False)
GPIO.setup(23,False)
time.sleep(0.7)

#Move forward again for approx 1.5 seconds
GPIO.setup(22,True)
time.sleep(1.5)

#Stop all movements
GPIO.setup(17,False)
GPIO.setup(22,False)