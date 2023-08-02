#just a file for general info and misc responses

def infoResponse(messageContent, author):
  textBlock = "This is a placeholder for general info when using !info"
  infoResponse = ("Hi! " + str(author) + " I am a simple bot for Molon. For a list of commands, type '!help'. For info about a specific command type !help <command>.")
  return textBlock
  #return infoResponse

def helpResponse(messageContent):
  listedResponses = ["test", "test2", "!help", "!info", "!roll <number>", "!suggestion"]
  #listedResponses = "List of commands: !info, !help, !roll, !points, !suggestion, , "
  # do we want it to be displayed as a list? Maybe just a string of the items instead?
  textBlock = "Placeholder for a list of different commands that the bot should be capable of doing"
#  return textBlock
  return listedResponses