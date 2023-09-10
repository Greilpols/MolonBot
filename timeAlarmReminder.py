#intended to be used for daily reminders, alarms as well as other time related things (i.e. temporarily silence someone)

import datetime
import time
import threading

def botTiming(messageContent): #'!timer' or '!reminder' or '!schedule'
  print(datetime.datetime.now())
  print("testTimerThing")
  return "Timer has been placed for 10s"

def testFunct():
  print("preprint")
  print(datetime.datetime.now())
  print("infunct")
  return "Bob"

def timerTest():
  return "Timer is up"