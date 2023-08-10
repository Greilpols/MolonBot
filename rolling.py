# Simply roll random number
import random
import databasing

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
    rolled = 'x'
  finally:
    return rolled

def deathRolling(roll, userName):
  result = tryingRolling(roll)
  #call to database if loss
  #return comment
  return "placeholder"