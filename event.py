import json
from time import time

class Event(object):

    def __init__(self, timeInSeconds = None, eventType = None):
        self.timeInSeconds = timeInSeconds or int(time())
        self.eventType = eventType or "AWAITING_FIRST_EVENT"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

