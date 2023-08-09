# Handling file suggestions, adding and just general usage of the suggestions.txt file


def suggestions(messageContent, action, userName):
  if (action == "add"):
    success = addSuggestion(messageContent)
    return success
  elif (action == "forget"):
    success = forgetSuggestion(messageContent, userName)
    return success
  return 0


def addSuggestion(messageContent):
  try:
    with open("suggestions.txt", "a") as f:
      f.write(messageContent + "\n")
    result = "Suggestion added!"
  except Exception:
    result = "Something went wrong. Please try again later."
  finally:
    return result


def forgetSuggestion(messageContent, userName):
  return "placeholder"