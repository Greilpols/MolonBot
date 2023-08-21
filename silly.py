import random

def silly(amusementType):
  if (amusementType == '!joke'):
    try:
      with open("silly.txt", "r") as f:
        jokes = f.readlines()
      return jokes[int(random.randrange(10))]
    except Exception:
      result = "Something went wrong. Please try again later."
    return result
  else:
    return "mirror"