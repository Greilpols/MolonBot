import random

def silly(amusementMessage, author):
  amusementType = amusementMessage.split(" ")[0]
  if (amusementType == '!joke'):
    try:
      if amusementMessage.split(" ")[1] == 'add':
        messageContent = amusementMessage.split(" ")
        messageContent.pop(0)
        messageContent.pop(0)
        addedJoke = " ".join(messageContent)
        with open("silly.txt", "a") as f:
          f.write("\n" + addedJoke + " - " + str(author))
        f.close()
        return "Joke added!"
      else:
        return printJoke()
    except Exception:
      return printJoke()
  else:
    return "mirror"


def printJoke():
  try:
    with open("silly.txt", "r") as f:
      jokes = f.readlines()
      fileLength = len(jokes)
      joke = jokes[random.randrange(fileLength)]
    return joke
  except Exception:
    return"Something went wrong. Please try again later."