from replit import db
#do I just make make a new variable to have username as string?

def addUser(user):
  if str(user) in db:
    return "user in db"
  else:
    try:
      db[str(user)] = 0
      return "user added to db"
    except Exception:
      return "user not in db, adding failed"

def showScore(user):
  print (str(user) + "testforuser")
  if str(user) in db:
    print (str(db[user]))
    return ("Your score is " + db[user])
  else:
    addUser(user)
    return ("Username not found in database. You have now been added. Your score is " + str(db[user]))
  return "Something went terribly wrong. Try again later. If problem persist, pester coder."

def addScore(userName, amount):
  #add this amount of points to the user
  try:
    points = int(amount)
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

def reduce(userName, amount):
  try:
    points = int(amount)
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