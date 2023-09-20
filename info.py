#just a file for general info and misc responses

def infoResponse(messageContent, author):
  return ("Hi! " + str(author) + " I am a simple bot for Molon. For a list of commands, type '!help'. For info about a specific command type !help <command>.")

def helpResponse(messageContent):
  return ("!info, !help, !roll <number>, !deathroll <bet value>, !suggestion, !score, !add, !reduce, !joke, !timer, !schedule (and more, it is WIP after all)")
  return listedResponses