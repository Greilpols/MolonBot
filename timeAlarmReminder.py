#intended to be used for daily reminders, alarms as well as other time related things (i.e. temporarily silence someone)

import datetime

def botTiming(messageContent, author): #'!timer' or '!reminder' or '!schedule'
  splitLine = messageContent.split(" ")
  try:
    timerLength = int(splitLine[1])
    if timerLength > 301 or timerLength < 1:
      return [1, "Error. Timer must be of appropriate length. (1-300s)"]
    #fix to be able to choose target
    print(datetime.datetime.now())
    return [2, ("Timer has been placed for " + str(timerLength) + " seconds"), author, timerLength]
  except ValueError:
    return [1, "Error. Number did not get extracted properly."]
  except Exception:
    return [1, "Error. Something unknown went wrong."]
  finally:
    return [1, "Unexpected outcome. Error that should not be accessible. Please poke me and tell me how you got this."]

def timerPoke(author):
  return ("Hey @" + author + "! Timer is up!")