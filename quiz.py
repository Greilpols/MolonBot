#use this to create the different quizes, cause why not?
#use DB to hold questions and answers, use names that 'players' won't have...
#

from replit import db
import random


def quiz(quizType):
    if quizType == warcraft:
        quizResponse = warcraftQuiz
    return quizResponse


def warcraftQuiz():
    randomNumber = random.randrange(5)
    warcraftResponse = [db[warcraft_Quiz][randomNumber], db[warcraft_QuizAnswers][randomNumber]]

    return warcraftResponse