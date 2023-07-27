# Handling file suggestions, adding and just general usage of the suggestions.txt file

def suggestions(messageContent, action):
  if (action == add):
    success = addSuggestion(messageContent)
    return success

def addSuggestion(messageContent):
  try:
    with open("suggestions.txt","a") as f:
      f.write(messageContent)
    success = "Suggestion added!"
  except Exception:
    success = "Something went wrong. Please try again later."
  finally:
    return success