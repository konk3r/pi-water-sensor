import json
import event_file_io
from time import time
from types import SimpleNamespace

class Event(object):
    timeInSeconds = 0,
    eventType = "awaiting_first_event"

    def __init__(self, timeInSeconds, eventType):
        self.timeInSeconds = timeInSeconds,
        self.eventType = eventType

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def manageIncomingEvent(eventTimeInSeconds):
    lastEvent = json.loads(event_file_io.loadLastEvent(), object_hook=lambda d: Event(**d))

    lastEvent.timeInSeconds = incomingEventTimeInSeconds
    eventJson = lastEvent.toJSON()

    print("Storing event from: " + str(incomingEventTimeInSeconds))
    event_file_io.storeLastEvent(eventJson)
    event_file_io.addEventToLogs(eventJson)


if __name__ == "__main__":
    incomingEventTimeInSeconds = int(time())
    manageIncomingEvent(incomingEventTimeInSeconds)
