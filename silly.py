import random

def silly(amusementMessage, author):
  amusementType = amusementMessage.split(" ")[0]
  if (amusementType == '!joke'):
    try:
      if amusementMessage.split(" ")[1] == 'add':
        messageContent = amusementMessage.split(" ")
        messageContent.pop(0)
        messageContent.pop(0)
        joke = ' '.join(messageContent)
        with open("silly.txt", "a") as f:
          f.write(messageContent + " - " + author + "\n")
        result = "Joke added!"
        f.closed
        return result
    except Exception:
      print(amusementMessage, author)
    try:
      with open("silly.txt", "r") as f:
        jokes = f.readlines()
        fileLength = len(jokes)
        joke = jokes[random.randrange(fileLength)]
      return joke
    except Exception:
      result = "Something went wrong. Please try again later."
    return result
  else:
    return "mirror"