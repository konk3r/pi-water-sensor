import pygame
from event import Event

ROOT_PATH = "/opt/casadetasha/water-alert/"
ALERT_AUDIO_PATH = ROOT_PATH + "redemption_song.mp3"

# SECONDS_IN_10_MINUTES = 60 * 10
SECONDS_IN_10_MINUTES = 5

def shouldNotifyWaterActivated(oldEvent, newEvent):
    offsetPreviousTime = oldEvent.timeInSeconds + SECONDS_IN_10_MINUTES

    if oldEvent.eventType == Event.WATER_FILLED:
        return False

    if offsetPreviousTime < newEvent.timeInSeconds and newEvent.eventType == Event.WATER_FILLED:
        return True
    else:
        return False

def notifyWaterAvailable():
    print("WATER HAS RETURNED")

    pygame.mixer.init()
    pygame.mixer.music.load(ALERT_AUDIO_PATH)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

