#intended to be used for daily reminders, alarms as well as other time related things (i.e. temporarily silence someone)

import datetime
import time
import threading

def botTiming(messageContent, author): #'!timer' or '!reminder' or '!schedule'
  splitLine = messageContent.split(" ")
  try:
    timerLength = int(splitLine[1])
    if timerLength > 301 or timerLength < 1:
      return [1, "Error. Timer must be of appropriate length."]
    #fix to be able to choose target
    print(datetime.datetime.now())
    return [2, ("Timer has been placed for " + str(timerLength) + " seconds"), author, timerLength]
  except ValueError:
    return "Error. NAN"
  except Exception:
    return "Error. Something went wrong."
  finally:
    return "Unexpected outcome. Error that should not be accessible."

def timerPoke(author):
  return ("Hey @" + author + "! Timer is up!")