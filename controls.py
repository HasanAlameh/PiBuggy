#Hasan Alameh's PiCart

#Import time & GPIO controller modules

import time
import RPi.GPIO as GP

#Using BroadCom channels for pin referencing
GP.setmode(GP.BCM)

#Disable any warnings script
GP.setwarnings(False)