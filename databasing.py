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
  try:
    amount = amountText.split(" ")
    number = amount[1]
    points = int(number)
  except ValueError:
    return "Error. Value must be a number."
  except Exception:
    return "Unknown error. if problem persists, do something else."
  if userName not in db:
    return "Error in database handling."
  elif amount < 0:
    return "Error. this is only for adding points, use !loss or !subtract instead."
  else:
    db[userName] = db[userName] + points
  return ("Your score is " + str(db[userName]))

def reduce(userName, amountText):
  #remove this amount of points from user
  try:
    amount = amountText.split(" ")
    number = amount[1]
    points = int(number)
  except ValueError:
    return "Error. Value must be a number."
  except Exception:
    return "Unknown error. if problem persists, do something else."
  if userName not in db:
    return "Error in database handling."
  elif amount < 0:
    return "Error. this is only for reducing points, use !add or !winning instead."
  else:
    db[userName] = db[userName] + points
  return ("Your score is " + str(db[userName]))