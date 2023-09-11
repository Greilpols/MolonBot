#intended to be used for daily reminders, alarms as well as other time related things (i.e. temporarily silence someone)

import datetime
import time
import threading

def botTiming(messageContent): #'!timer' or '!reminder' or '!schedule'
  splitLine = messageContent.split(" ")
  timerLength = splitLine[1]
  try:
    response = ["test", "123"]
    print(datetime.datetime.now())
    return "Timer has been placed for 10s"
  except ValueError:
    return "Error. NAN"
  except Exception:
    return "Error. Something went wrong."
  finally:
    return "Unexpected outcome. Error that should be accessible."

def timerPoke(author):
  return ("Hey @" + author + "! Timer is up!")