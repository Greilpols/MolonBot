import os
import discord
import requests
import json
import time
import threading
import asyncio
import datetime
from discord.ext import tasks

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

messageTime = 230000


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  minuteChecker.start()
  hourChecker.start()


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
    sillyResponse = silly.silly(message.content, message.author)
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

  elif message.content.startswith('!timer') or message.content.startswith('!reminder') or message.content.startswith('!schedule'):  # do we just thread the whole thing? Seems asyncio is the way to go!
    timeResponse = timeAlarmReminder.botTiming(message.content, message.author)
    #figure out why switches refuse to work here
    #timeresponse = [enum, text, pokes, timedelay]
    if timeResponse[0] == 1:  #some error
      await message.channel.send(timeResponse[1])
    elif timeResponse[0] == 2:
      await message.channel.send(timeResponse[1])
      await asyncio.sleep(timeResponse[3])
      await message.channel.send(timeAlarmReminder.timerPoke(timeResponse[2]))
    else:
      await message.channel.send("Something went very wrong. Timer sadly not working at the moment.")

#for timecheckers it uses GMT time, so adjust +3 for local
@tasks.loop(minutes=1)
async def minuteChecker():
  now = datetime.datetime.now()
  current_time = now.strftime("%H:%M")  # H - hour, M- minute, S - second
  print(datetime.datetime.now())
  print("Current Time =", current_time)
  if current_time == "13:02":
    print("ding dong")

@tasks.loop(minutes=60)
async def hourChecker():
  now = datetime.datetime.now()
  current_time = now.strftime("%H")  # H - hour, M- minute, S - second
  print(datetime.datetime.now())
  print("Current Time =", current_time)
  if current_time == "13":
    print("The clock is 13 (something)") #this will drift as it starts at different hours - only use for things where which minute of the hour doesn't matter


keep_alive()
client.run(os.getenv('TOKEN'))
