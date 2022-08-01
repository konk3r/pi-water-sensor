# SECONDS_IN_10_MINUTES = 60 * 10
SECONDS_IN_10_MINUTES = 5

def shouldNotifyWaterActivated(oldEvent, newEvent):
    offsetPreviousTime = oldEvent.timeInSeconds + SECONDS_IN_10_MINUTES
    if offsetPreviousTime < newEvent.timeInSeconds:
        return True
    else:
        return False

def notifyWaterAvailable():
    print("WATER UPDATED")
    print("WATER UPDATED")
    print("WATER UPDATED")
    print("WATER UPDATED")
    print("WATER UPDATED")
    print("WATER UPDATED")
    print("WATER UPDATED")
