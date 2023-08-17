#use this to create the different quizes, cause why not?
#use DB to hold questions and answers, use names that 'players' won't have...
#

from replit import db
import random

quizType = 'Uninitialized'
quizCounter = 0
quizQuestionsNotAsked = []

#reseting all details of the quiz before starting
def quiz(quizTypeToStart):
  global quizCounter
  quizCounter = 0
  global quizType
  quizType = quizTypeToStart
  global quizQuestionsNotAsked
  quizQuestionsNotAsked = []
  for i in db[quizType]:
    quizQuestionsNotAsked.append(i-1) #should give 0->n in list, no? Doublecheck..
  return ("Now starting a quiz of the " + quizType + " variety!")

def nextQuestion():
  #for next question, so keep continuing on the same quiz
  global quizCounter
  quizCounter += 1
  global quizQuestionsNotAsked
  randomNumber = random.choice(quizQuestionsNotAsked) #temp value for testing - WIP change number to num of q's available
  quizQuestionsNotAsked.pop(randomNumber)
  if quizType == "Uninitialized":
    return ["No quiz type started. write !quiz <type> to start one"]

  warcraftResponse = [db[warcraft_Quiz][randomNumber], db[warcraft_QuizAnswers][randomNumber]]

  return warcraftResponse

def warcraftQuiz():
  randomNumber = random.randrange(5)
  quizType = "Warcraft"
  warcraftResponse = ["This will start a World of Warcraft quiz!", db[warcraft_Quiz][randomNumber], db[warcraft_QuizAnswers][randomNumber]]
  print (quizCounter)

  return warcraftResponse

def addToQuiz(question, answer):
  global quizType
  if quizType == "Uninitialized":
    return "Error: Quiztype uninitialized."
  quizTypeAnswers = quizType + "Answers"
  db[quizType].append(question)
  db[quizTypeAnswers].append(answer)
  return ((question) + " has been added as a question and " + (answer) + " as the answer to the quiz of " + (quizType))
  
  