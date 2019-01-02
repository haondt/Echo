# Echo is a Discord bot

import discord

with open('token.txt') as tokenfile:
	token = tokenfile.read().strip()

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-'*10)

@client.event
async def on_message(message):
	# don't let bot reply to itself
	if message.author != client.user:
		if message.content.startswith('!hello'):
			await client.send_message(message.channel, 'Moshi moshi')

client.run(token)
