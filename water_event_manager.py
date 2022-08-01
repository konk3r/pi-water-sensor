import json
import event_file_io
from event import Event
from water_notifier import shouldNotifyWaterActivated, notifyWaterAvailable

def manageIncomingEvent(eventTimeInSeconds):
    lastEvent = event_file_io.loadLastEvent()

    newEvent = Event(timeInSeconds = eventTimeInSeconds, eventType = "WATER_DETECTED")
    eventJson = newEvent.toJSON()

    print("Storing event from: " + str(eventTimeInSeconds))
    event_file_io.storeLastEvent(eventJson)
    event_file_io.logLastEvent(eventJson)

    print("Checking water updated alert")
    if shouldNotifyWaterActivated(lastEvent, newEvent):
        notifyWaterAvailable()

