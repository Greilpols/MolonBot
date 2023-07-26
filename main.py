import os
import discord
import requests
import json
import info
import random
import rolling

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
    messageResponse = info.infoResponse(message.content)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!help'):
    messageResponse = info.helpResponse(message.content)
    await message.channel.send(messageResponse)

  elif message.content.startswith('!roll'):
    messageResponse = rolling.rollingFunctions(message.content)
    await message.channel.send(messageResponse)

keep_alive()
client.run(os.getenv('TOKEN'))