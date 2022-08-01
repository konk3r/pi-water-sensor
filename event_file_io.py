import json
from os.path import exists as file_exists
from event import Event

ROOT_PATH = "/var/casadetasha/water-alert/"
EVENT_LOGS_FILE_PATH = ROOT_PATH + "collection_event_logs.txt"
LAST_EVENT_FILE_PATH = ROOT_PATH + "last_collection_event.txt"

def loadLastEvent():
    if file_exists(LAST_EVENT_FILE_PATH):
        textFile = open(LAST_EVENT_FILE_PATH, "r")
        lastEventData = textFile.read()
        textFile.close()

        lastEvent = json.loads(lastEventData, object_hook=lambda d: Event(**d))
    else:
        lastEvent = Event(timeInSeconds = -1)

    print("LoadedEvent: " + lastEvent.eventType + " | time: " + str(lastEvent.timeInSeconds))
    return lastEvent

def storeLastEvent(event):
    textFile = open(LAST_EVENT_FILE_PATH, "w")
    textFile.write(event + "\n")
    textFile.close()

def logLastEvent(event):
    textFile = open(EVENT_LOGS_FILE_PATH, "a")
    textFile.write(event + "\n\n------------\n\n")
    textFile.close()

