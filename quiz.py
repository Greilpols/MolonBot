#use this to create the different quizes, cause why not?
#use DB to hold questions and answers, use names that 'players' won't have...
#

from replit import db
import random

quizType = "Nothing"
quizCounter = 0

def quiz(quizType):
    if quizType == warcraft:
        quizResponse = warcraftQuiz
    return quizResponse

def nextQuestion():
    #for next question, so keep continuing on the same quiz
    randomNumber = random.randrange(5)
    warcraftResponse = [db[warcraft_Quiz][randomNumber], db[warcraft_QuizAnswers][randomNumber]]

    return warcraftResponse

def warcraftQuiz():
    randomNumber = random.randrange(5)
    quizType = "Warcraft"
    quizCounter += 1
    warcraftResponse = ["This will start a World of Warcraft quiz!", db[warcraft_Quiz][randomNumber], db[warcraft_QuizAnswers][randomNumber]]
    print (quizCounter)

    return warcraftResponse