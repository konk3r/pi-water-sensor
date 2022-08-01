import json
import event_file_io
from event import Event
from water_notifier import shouldNotifyWaterActivated, notifyWaterAvailable

def shouldStoreIncomingEvent(oldEvent, newEvent):
    if oldEvent.eventType == newEvent.eventType:
        print("Event types are equal")
        return False
    else:
        return True

def processEvents(eventTimeInSeconds, oldEvent, newEvent):
    print("New event: " + newEvent.eventType)
    eventJson = newEvent.toJSON()

    if shouldStoreIncomingEvent(oldEvent, newEvent):
        print("Storing event from: " + str(eventTimeInSeconds))
        event_file_io.storeLastEvent(eventJson)
        event_file_io.logLastEvent(eventJson)
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

