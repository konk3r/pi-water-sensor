import RPi.GPIO as GPIO

GPIO_CHANNEL = 10

def startSensorSetup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def addSensorEventCallback(callback):
    GPIO.add_event_detect(GPIO_CHANNEL, GPIO.BOTH, callback=callback)

def endSensorSetup():
    GPIO.cleanup()

def sensorIsActive():
    return GPIO.input(GPIO_CHANNEL) > 0

