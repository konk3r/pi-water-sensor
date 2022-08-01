from time import time
from water_event_manager import manageIncomingEvent

if __name__ == "__main__":
    incomingEventTimeInSeconds = int(time())
    manageIncomingEvent(incomingEventTimeInSeconds)

