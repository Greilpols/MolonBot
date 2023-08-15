import os
import discord
import requests
import json
import time

import info
import suggestions
import random
import rolling
import databasing
import silly
import quiz
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
    messageResponse = suggestions.suggestions(message.content, "add")
    await message.channel.send(messageResponse)

  elif message.content.startswith('!forget'):
    messageResponse = suggestions.suggestions(message.content, "forget")
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

  elif message.content.startswith('!silly'):
    sillyResponse = "Two monkeys."
    await message.channel.send(sillyResponse)

  elif message.content.startswith('!quiz'):
    #placeholder quiztype for testing stuffs:
    quizType = 'warcraft'
    quizResponse = quiz.quiz(quizType)
    await message.channel.send(quizResponse[0])
    time.sleep(5)
    await message.channel.send("The correct answer is " + str(quizResponse[1]))
    #how to check and set up checking correct answers on quiz? Will have to check and smooth out.

  elif message.content.startswith('!next'):
    quizResponse = quiz.next()
    await message.channel.send(quizResponse[0])
    time.sleep(5)
    await message.channel.send("The correct answer is " + str(quizResponse[1]))

keep_alive()
client.run(os.getenv('TOKEN'))