import random

def silly(amusementMessage):
  amusementType = amusementMessage.split(" ")[0]
  if (amusementType == '!joke'):
    try:
      if amusementMessage.split(" ")[1] == add:
        with open("silly.txt", "a") as f:
          f.write(userName + messageContent + "\n")
        result = "Joke added!"
        f.closed
        return result
    except Exception:
      print(amusementMessage)
    try:
      with open("silly.txt", "r") as f:
        jokes = f.readlines()
        fileSize=len([0 for _ in f])
        joke = jokes[int(random.randrange(fileSize))]
      return joke
    except Exception:
      result = "Something went wrong. Please try again later."
    return result
  else:
    return "mirror"