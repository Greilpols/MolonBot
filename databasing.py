from replit import db

def addUser(userName):
  if userName in db:
    print ("Error. User already in db. Should have been picked up already.")
    return "Error.  Something's not working as it should."
  else:
    try:
      db[userName] = 0
      return "user added to db"
    except Exception:
      return "user not in db, adding failed"

def showScore(user):
  userName = str(user)
  print (userName + " User requesting showing score.")
  if userName in db:
    print (db[userName])
    return ("Your score is " + str(db[userName]))
  else:
    addUser(userName)
    return ("Username not found in database. You have now been added. Your score is " + str(db[userName]))
  return "Something went terribly wrong. Try again later. If problem persist, pester coder."

def addScore(userName, amountText):
  #add this amount of points to the user
  num = checkNumber(amountText)
  if num == 0:
    return "Not a number"
  elif num == "x":
    return "Unknown error. if problem persists, do something else."
  if userName not in db:
    return "Error in database handling."
  else:
    db[userName] = db[userName] + points
  return ("Your score is " + str(db[userName]))

def reduce(userName, amountText):
  #remove this amount of points from user
  num = checkNumber(amountText)
  if num == 0:
    return "Not a number"
  elif num == "x":
    return "Unknown error. if problem persists, do something else."
  if userName not in db:
    return "Error in database handling."
  else:
    db[userName] = db[userName] + points
  return ("Your score is " + str(db[userName]))


def checkNumber(message):
  try:
    splitLine = message.split(" ")
    number = int(splitLine[1])
  except ValueError:
    print("Error. Not a number.")
    return 0
  except Exception:
    return "x"
  return number