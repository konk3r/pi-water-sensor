import json
from os.path import exists as file_exists
from event import Event

ROOT_PATH = "/var/casadetasha/water-alert/"
EVENT_LOGS_FILE_PATH = ROOT_PATH + "collection_event_logs.txt"
LAST_EVENT_FILE_PATH = ROOT_PATH + "last_collection_event.txt"

def isEventFillRelated(event):
    eventType = event.eventType
    return eventType == Event.WATER_FILLED or eventType == Event.WATER_DRAINED

def loadLastRecordedEvent():
    if file_exists(LAST_EVENT_FILE_PATH):
        textFile = open(LAST_EVENT_FILE_PATH, "r")
        lastRecordedEventData = textFile.read()
        textFile.close()

        lastRecordedEvent = json.loads(lastRecordedEventData, object_hook=lambda d: Event(**d))
    else:
        lastRecordedEvent = Event(timeInSeconds = -1)

    print("LoadedEvent: " + lastRecordedEvent.eventType + " | time: " + str(lastRecordedEvent.timeInSeconds))
    return lastRecordedEvent

def storeLastEvent(event):
    if isEventFillRelated(event):
        textFile = open(LAST_EVENT_FILE_PATH, "w")
        textFile.write(event.toJSON() + "\n")
        textFile.close()
    else:
        print("Attempting to store non-fill related event. Ignoring.")

def logEvent(event):
    textFile = open(EVENT_LOGS_FILE_PATH, "a")
    textFile.write(event.toJSON() + "\n\n------------\n\n")
    textFile.close()

