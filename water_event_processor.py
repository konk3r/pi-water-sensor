import json
from time import time
import event_file_io
from event import Event
from water_notifier import shouldNotifyWaterActivated, notifyWaterAvailable
from gpio_sensor import sensorIsActive

def processCurrentConnection(channel):
    incomingEventTimeInSeconds = int(time())

    if sensorIsActive():
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_FILLED)
    else:
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_DRAINED)

def connection_changed(channel):
    incomingEventTimeInSeconds = int(time())

    if GPIO.input(GPIO_CHANNEL) > 0:
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_FILLED)
    else:
        manageIncomingEvent(incomingEventTimeInSeconds, Event.WATER_DRAINED)

def processWake():
    wakeEvent = Event(eventType = Event.WAKE_UP)
    event_file_io.logEvent(wakeEvent)


def shouldStoreIncomingEvent(oldEvent, newEvent):
    if oldEvent.eventType == newEvent.eventType:
        print("Event types are equal")
        return False
    else:
        return True

def processEvents(eventTimeInSeconds, oldEvent, newEvent):
    print("New event: " + newEvent.eventType)

    if shouldStoreIncomingEvent(oldEvent, newEvent):
        print("Storing event from: " + str(eventTimeInSeconds))
        event_file_io.storeLastEvent(newEvent)
        event_file_io.logEvent(newEvent)
    else:
        print("Not storing event")

    print("Checking water updated alert")
    if shouldNotifyWaterActivated(oldEvent, newEvent):
        notifyWaterAvailable()

    print("")
    print("")

def manageIncomingEvent(eventTimeInSeconds, incomingEventType):
    oldEvent = event_file_io.loadLastRecordedEvent()
    newEvent = Event(timeInSeconds = eventTimeInSeconds, eventType = incomingEventType)

    processEvents(eventTimeInSeconds, oldEvent, newEvent)

