import discord
import soup
from command_handler import CommandHandler
import os

token = os.environ['TOKEN']

client = discord.Client()
diy_list = soup.get_diy_list()
ch = CommandHandler(client)

# Not entirely sure what this method does but it was in the tutorial and I'm afraid to remove it
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

# Method for sending message when author message starts with !diy
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!ribbot'):
		await ch.command_handler(message)

# ====================
# describe diy
# ====================
# function
def describe_diy(message, client, diy_name):
	if( len(diy_name) == 0 ):
		return 'Missing 1 argument.'
	
	item = diy_name[0].lower()
	found = False
	for tag in diy_list:
		if( tag.find("th") ):
			continue
		name = soup.get_name(tag).lower()
		if(name == item):
			found = True
			reply = soup.get_all(tag)
			e = discord.Embed(title=reply[0],color=16098851)
			e.set_image(url=soup.get_img_url(tag))
			e.add_field(name="Sell Price", value=reply[1], inline=False)
			e.add_field(name="Type", value=reply[2], inline=False)
			e.add_field(name="Materials Needed", value=reply[3], inline=False)
			e.add_field(name="Source", value=reply[4], inline=False)
			return message.channel.send(embed=e)
			break
	if(not found):
		return 'Item not found. Please try again!'
# dictionary
ch.add_command({
	'trigger': 'diy',
	'function': describe_diy,
	'description': 'Will return a description of the DIY recipe.'
})
# ====================
# end describe diy
# ====================

client.run(token)