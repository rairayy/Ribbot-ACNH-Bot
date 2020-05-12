import discord
import soup
from bs4 import BeautifulSoup
import os

token = os.environ['TOKEN']

client = discord.Client()
diy_list = soup.get_diy_list()

# Not entirely sure what this method does but it was in the tutorial and I'm afraid to remove it
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

# Method for sending message when author message starts with !diy
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!diy'):
		msg = message.content.split(" ",1)
		
		#validate
		if(len(msg) < 2):
			await message.channel.send('Please follow this format for your messages: `!diy <item>`')
			return
		
		item = msg[1].lower()
		
		found = False
		for tag in diy_list:
			if( tag.find("th") ):
				continue
			name = soup.get_name(tag).lower()
			if(name == item):
				found = True
				reply = soup.get_all(tag)
				e = discord.Embed()
				e.set_image(url=soup.get_img_url(tag))
				await message.channel.send(reply, embed=e)
				break
		
		if(not found):
			await message.channel.send('Item not found. Please try again!')

client.run(token)