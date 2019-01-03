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
		text_channel = message.channel
		server = message.server
		voice_channel = message.author.voice.voice_channel

		if message.content.startswith('!hello'):
			await client.send_message(text_channel, 'Moshi moshi')
			return
		
		elif message.content.startswith('!play'):
			# get the voice client for this server
			voice_client = client.voice_client_in(server)

			# ensure user is in a voice and text channel
			if server == None or text_channel == None:
				return
			elif voice_channel == None:
				await client.send_message(text_channel, 'You must be in a voice channel for me to play music')
				return 

			# check if client is already in a voice channel
			if client.is_voice_connected(server):

				# client is in a different voice channel
				if voice_client.channel != voice_channel:
					await client.send_message(message.channel, 'I\'m already ~~Tracer~~ in a different voice channel')
					return

			# join users voice channel if not already in it
			else:
				voice_client = await client.join_voice_channel(voice_channel)
			
			
			await client.send_message(message.channel, 'Added %s to queue' % message.content)


# leave voice channel if it is in there all by itself
@client.event
async def on_voice_state_update(before, after):
	channel = before.voice.voice_channel
	if channel != None:
		server = channel.server
		if channel != None:
			if client.is_voice_connected(server):
				voice_client = client.voice_client_in(server)
				if voice_client.channel == channel:
					if len(channel.voice_members) < 2:
						await voice_client.disconnect()
				
		

client.run(token)
