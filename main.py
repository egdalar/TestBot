import discord

client = discord.client()

@client.event
async def on_ready():
  print('Moo {0.user}'.format(Client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.starrtswith('/hello');
   await message.channel.send('hello!')

client.run()
