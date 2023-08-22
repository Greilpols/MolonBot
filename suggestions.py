# Handling file suggestions, adding and just general usage of the suggestions.txt file


def suggestions(messageContent, action, userName):
  if (action == "add"):
    success = addSuggestion(messageContent, userName)
    return success
  elif (action == "forget"):
    success = forgetSuggestion(messageContent, userName)
    return success
  return 0


def addSuggestion(messageContent, userName):
  try:
    with open("suggestions.txt", "a") as f:
      f.write(userName + messageContent + "\n")
    result = "Suggestion added!"
    f.closed
  except Exception:
    result = "Something went wrong. Please try again later."
  finally:
    return result


def forgetSuggestion(messageContent, userName):
  try:
    with open("suggestions.txt", "rw") as f:
      suggestText = f.read()
      for line in suggestText:
        if line.startswith(userName):
          pass
        else:
          f.write(line) #this needs testing before implementing: fear is it might just overwrite without copying all lines etc
          return ("Suggestions by " + userName + " has been removed.")
  except Exception:
    return "placeholder"