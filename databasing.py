from replit import db

def addUser(user):
  if user in db:
    return "user in db"
  else:
    try:
      db[user] = 0
      return "user added to db"
    except Exception:
      return "user not in db, adding failed"

def showScore(user):
  print (user + "testforuser")
  if user in db:
    print (db[user])
    return ("Your score is " + db[user])
  else:
    addUser(user)
    return ("Username not found in database. You have now been added. Your score is " + db[user])
  return "Something went terribly wrong. Try again later. If problem persist, pester coder."