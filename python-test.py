import json
from time import time
from os.path import exists as file_exists

ROOT_PATH = "/var/casadetasha/water-alert/"
EVENT_LOGS_FILE_PATH = ROOT_PATH + "collection_event_logs.txt"
LAST_EVENT_FILE_PATH = ROOT_PATH + "last_collection_event.txt"
TEN_MINUTES_TO_SECONDS = 60*10

BLANK_EVENT_JSON = json.dumps({
        "eventTimeInSeconds": 0,
        "eventType": "awaiting_first_event"
})

if file_exists(LAST_EVENT_FILE_PATH):
    textFile = open(LAST_EVENT_FILE_PATH, "r")
    fileContent = textFile.read()
    textFile.close()
else:
    fileContent = BLANK_EVENT_JSON

print("Loading " + fileContent)
workingJson = json.loads(fileContent)
loadedTimeString = str(workingJson["eventTimeInSeconds"])

print("Last loaded time: " + loadedTimeString)

workingJson["eventTimeInSeconds"] = int(time())

textFile = open(LAST_EVENT_FILE_PATH, "w")
textFile.write(json.dumps(workingJson) + "\n")
textFile.close()

textFile = open(EVENT_LOGS_FILE_PATH, "a")
textFile.write(json.dumps(workingJson) + "\n\n------------\n\n")
textFile.close()

