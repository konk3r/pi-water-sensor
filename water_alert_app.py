from time import time
from event import Event
from water_event_manager import manageIncomingEvent, processWake
from gpio_sensor import startSensorSetup, addSensorEventCallback, endSensorSetup, sensorIsActive, GPIO_CHANNEL

def processCurrentConnection(channel):
    incomingEventTimeInSeconds = int(time())

    if sensorIsActive():
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_FILLED)
    else:
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_DRAINED)

def manageSensor():
    startSensorSetup()
    addSensorEventCallback(processCurrentConnection)
    processCurrentConnection(GPIO_CHANNEL)
    endSensorSetup()


if __name__ == "__main__":
    processWake()
    manageSensor()
    message = input("Press enter to quit\n\n")

