import os
import discord
import requests
import json
import time
import threading
import asyncio

import info
import suggestions
import random
import rolling
import databasing
import silly
import quiz
import timeAlarmReminder
from keep_alive import keep_alive

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')
    time.sleep(2)
    await message.channel.send('How can I help you?')

  elif message.content.startswith('!info'):
    messageResponse = info.infoResponse(message.content, message.author)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!help'):
    messageResponse = info.helpResponse(message.content)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!suggestion'):
    #need to add what kind of operation for suggestions
    #aka same as refactor and combine different suggestion
    messageResponse = suggestions.suggestions(message.content, "add", message.author)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!forget'):
    messageResponse = suggestions.suggestions(message.content, "forget", message.author)
    await message.channel.send("placeholder")

  elif message.content.startswith('!display'):
    messageResponse = suggestions.display(message.content, "display")
    await message.channel.send(messageResponse)

  elif message.content.startswith('!roll'):
    messageResponse = rolling.rollingFunctions(message.content)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!deathroll'):
    messageResponse = rolling.deathRolling(message.content, message.author)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!score'):
    databasingResponse = databasing.showScore(message.author)
    await message.channel.send(databasingResponse)

  # refactor and combine the different add/reduce etc commands for databasing
  elif message.content.startswith('!add'):
    databasingResponse = databasing.addScore(message.author, message.content)
    await message.channel.send(databasingResponse)

  elif message.content.startswith('!reduce'):
    databasingResponse = databasing.reduceScore(message.author, message.content)
    await message.channel.send(databasingResponse)

  elif message.content.startswith('!silly') or message.content.startswith('!joke'):
    sillyResponse = silly.silly(message.content)
    await message.channel.send(sillyResponse)

  elif message.content.startswith('!quiz'):
    quizResponse = quiz.quiz(message.content)
    await message.channel.send(quizResponse)
    #how to check and set up checking correct answers on quiz? Will have to check and smooth out.

  elif message.content.startswith('!next'):
    quizResponse = quiz.nextQuestion()
    await message.channel.send(quizResponse[0])
    await asyncio.sleep(10)
    await message.channel.send("The correct answer is " + str(quizResponse[1]))

  elif message.content.startswith('!removequiz'):
    quizResponse = quiz.removeFromQuiz(message.content)
    await message.channel.send(quizResponse)

  elif message.content.startswith('!timer') or message.content.startswith('!reminder') or message.content.startswith('!schedule'): # do we just thread the whole thing? Seems asyncio is the way to go!
    timeResponse = timeAlarmReminder.botTiming(message.content, message.author)
    test12334 = timeResponse[0]
    #figure out why switches refuse to work here
#timeresponse = [enum, text, pokes, timedelay]
    if timeResponse[0] == 1: #some error
      await message.channel.send(timeResponse[1])
    elif timeResponse[0] == 2:
      await message.channel.send(timeResponse[1])
      await asyncio.sleep(timeResponse[3])
      await message.channel.send(timeAlarmReminder.timerPoke(timeResponse[2]))
    else:
      await message.channel.send("Something went very wrong. Timer sadly not working at the moment.")

keep_alive()
client.run(os.getenv('TOKEN'))
