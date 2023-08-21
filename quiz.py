#use this to create the different quizes, cause why not?
#use DB to hold questions and answers, use names that 'players' won't have...
#

from replit import db
import random

quizType = 'Uninitialized'
quizCounter = 0
quizQuestionsNotAsked = []

#reseting all details of the quiz before starting
def quiz(quizTypeToStartContent):
  quizTypeToStart = quizTypeToStartContent.split(" ")[1] #Hmm, needs testing to see if needs to check if the quizzes exist/have enough questions or if works fine
  global quizCounter
  quizCounter = 0
  global quizType
  quizType = (quizTypeToStart + "_Quiz")
  global quizQuestionsNotAsked
  quizQuestionsNotAsked = []
  for i in db[quizType]:
    quizQuestionsNotAsked.append(i-1) #should give 0->n in list, no? Doublecheck..
  return ("Now starting a quiz of the " + quizTypeToStart + " variety!")

def nextQuestion():
  #for next question, so keep continuing on the same quiz
  global quizCounter
  quizCounter += 1
  global quizQuestionsNotAsked
  randomNumber = random.choice(quizQuestionsNotAsked) #temp value for testing - WIP change number to num of q's available
  quizQuestionsNotAsked.pop(randomNumber)
  if quizType == "Uninitialized":
    return ["No quiz type started. write !quiz <type> to start one"]
  nextQuestion[0] = db[quizType][randomNumber]
  nextQuestion[1] = db[(quizType)+"Answer"][randomNumber]
  return nextQuestion

def addToQuiz(question, answer):
  global quizType
  if quizType == "Uninitialized":
    return "Error: Quiztype uninitialized."
  quizTypeAnswers = quizType + "Answers"
  db[quizType].append(question)
  db[quizTypeAnswers].append(answer)
  return ((question) + " has been added as a question and " + (answer) + " as the answer to the quiz of " + (quizType))
  
def removeFromQuiz(messageContent):
  try:
    splitLine = messageContent.split(" ")
    number = int(splitLine[1])
    number = number - 1
  except ValueError:
    return "Error. Not a number of a question to remove. Please put number of question to remove."
  except Exception:
    return "Unknown error. Please add what went wrong as a suggestion."
  global quizType
  if quizType == "Uninitialized":
    return "Error: Quiztype uninitialized."
  quizTypeAnswers = quizType + "Answers"
  db[quizType].pop(number)
  db[quizTypeAnswers].append(number)
  return ("Question has been removed as a question and as the answer to the quiz of " + (quizType))