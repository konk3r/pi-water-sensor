from time import time
from event import Event
from water_event_manager import manageIncomingEvent
import RPi.GPIO as GPIO

GPIO_CHANNEL = 10

def connection_changed(channel):
    incomingEventTimeInSeconds = int(time())

    if GPIO.input(GPIO_CHANNEL) > 0:
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_FILLED)
    else:
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_DRAINED)


if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(GPIO_CHANNEL, GPIO.BOTH, callback=connection_changed)
    connection_changed(GPIO_CHANNEL)

    message = input("Press enter to quit\n\n")
    GPIO.cleanup()

