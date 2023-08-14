#use this to create the different quizes, cause why not?
#use DB to hold questions and answers, use names that 'players' won't have...
#

from replit import db
import random


def quiz(quizType):
    return "placeholder"


def warcraftQuiz():
    warcraftResponse = db[warcraftQuiz][int(random.randrange(5))]
    return warcraft