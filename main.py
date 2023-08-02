import os
import discord
import requests
import json
import info
import suggestions
import random
import rolling
import databasing
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

  elif message.content.startswith('!info'):
    messageResponse = info.infoResponse(message.content, message.author)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!help'):
    messageResponse = info.helpResponse(message.content)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!suggestion'):
    #need to add what kind of operation for suggestions
    messageResponse = suggestions.suggestions(message.content, "add")
    await message.channel.send(messageResponse)

  elif message.content.startswith('!roll'):
    messageResponse = rolling.rollingFunctions(message.content)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!score'):
    databasingResponse = databasing.showScore(message.author)
    await message.channel.send(databasingResponse)

keep_alive()
client.run(os.getenv('TOKEN'))