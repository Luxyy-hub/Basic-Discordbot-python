import discord
import os
import requests

client = discord.Client()

@client.event 
async def on_ready():
  print('BotName is logged in {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
     return

    if message.content.startswith('?hello'):
      await message.channel.send('Hi!')

client.run('BOT-TOKEN')
