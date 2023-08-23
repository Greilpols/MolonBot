#intended to be used for daily reminders, alarms as well as other time related things (i.e. temporarily silence someone)

import datetime
import time


def botTiming(messageContent): #'!timer' or '!reminder' or '!schedule'
  print(datetime.datetime.now())
  time.sleep(30) #test
  #nah need a better way than this...
  print(datetime.datetime.now())
  return "placeholder"