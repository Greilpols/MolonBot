#just a file for general info and misc responses

def infoResponse(messageContent, author):
  return ("Hi! " + str(author) + " I am a simple bot for Molon. For a list of commands, type '!help'. For info about a specific command type !help <command>.")

def helpCommands(messageContent):
  return ("Available commands: !info, !help, !roll <number>, !deathroll <bet value>, !suggestion, !score, !add, !reduce, !joke, !timer, !schedule (and more, it is WIP after all)")

def helpResponse(helpType):
  try:
    message = helpType.split(" ")[1]
    #temp return messages as things be set up WIP
    try:
      if message == '!info':
        return '!info message'
      elif message == '!help':
        return '!help message'
      elif message == '!roll':
        return '!roll message'
      elif message == '!deathroll':
        return '!deathroll message'
      elif message == '!suggestion':
        return '!suggestion message'
      elif message == '!score':
        return '!score message'
      elif message == '!add':
        return '!add message'
      elif message == '!reduce':
        return '!reduce message'
      elif message == '!joke':
        return '!joke message'
      elif message == '!timer':
        return '!timer message'
      elif message == 'schedule':
        return '!schedule message'
      else:
        return "Unfamiliar help request. Please tell me which message you tried to use."
    except Exception:
      return "Attempting to find help command failed. Not sure what you did to break this."
  except Exception:
    return helpCommands()