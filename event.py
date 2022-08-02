import json
from time import time
from datetime import datetime

class Event(object):
    WAKE_UP = "DEVICE_WAKE_UP"
    WATER_FILLED = "WATER_DETECTED"
    WATER_DRAINED = "WATER_DRAINED"
    AWAITING_FIRST_WATER_EVENT = "AWAITING_FIRST_WATER_EVENT"

    def __init__(self, timeInSeconds = None, eventType = None, processingDateTime = None):
        self.timeInSeconds = timeInSeconds or int(time())
        self.eventType = eventType or AWAITING_FIRST_WATER_EVENT
        self.processingDateTime = processingDateTime or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

