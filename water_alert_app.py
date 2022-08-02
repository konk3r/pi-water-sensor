from event import Event
from water_event_processor import manageIncomingEvent, processWake, processCurrentConnection
from gpio_sensor import setupSensor, addSensorEventCallback, teardownSensor

def startSensor():
    setupSensor()
    addSensorEventCallback(processCurrentConnection)
    processCurrentConnection(None)

if __name__ == "__main__":
    processWake()

    startSensor()
    message = input("Press enter to quit\n\n")
    teardownSensor()

