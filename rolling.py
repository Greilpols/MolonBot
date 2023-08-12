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
    #if failed to get number, just /roll 100
    print("Failure to get int")
    rolled = random.randrange(100)
  finally:
    return rolled

def deathRolling(roll, userName):
  result = tryingRolling(roll)
  #call to database if loss
  #return comment
  points = 100 #temp while deciding how to hold orig num... just use a list or summit? only want ganes to be temp after all
  gameWinner = "placeholderman"
  if result == 0:
    databasing.reduce(userName, points)
    databasing.add(gameWinner, points)
    return ("Victory! " + gameWinner + " has bested " + userName + "! " + points + " points to " + gameWinner + "!")
  return ("Let the games... be under way!")
  # note to self - do we want to use something silly as molonbucks or gold or?