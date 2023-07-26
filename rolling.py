# Simply roll random number
import random

def rollingFunctions(messageContent):
  splitLine = messageContent.split(" ")
  number = tryingRolling(splitLine[1])
  return number

def tryingRolling(roll):
  try:
    num = int(roll)
    rolled = random.randrange(num)
    print(rolled)
  except Exception:
    print("Failure to get int")
    rolled = '0'
  finally:
    return rolled
