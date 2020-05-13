import discord
import diy_parser
from command_handler import CommandHandler
import os

token = os.environ['TOKEN']
color = 16098851

client = discord.Client()
diy_list = diy_parser.get_diy_masterlist()
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
def describe_diy(message, client, args):
	if( len(args) == 0 ):
		return message.channel.send('Zzrrbbitt! Please follow this format for DIY requests: `!ribbot diy <item name>`')
	
	item = args[0].lower()
	found = False
	for i in diy_list:
		if( item == i[0].lower() ):
			found = True
			e = discord.Embed(title=i[0],color=color)
			e.set_image(url=i[1])
			e.add_field(name="Materials Needed", value='\n'.join(i[2]), inline=False)
			e.set_thumbnail(url=i[3])
			e.add_field(name="Obtained From", value=i[4], inline=False)
			e.add_field(name="Sell Price", value=i[5], inline=False)
			e.add_field(name="Type", value=i[6], inline=False)
			return message.channel.send(embed=e)
			break
	if(not found):
		return message.channel.send('Item not found. Please try again. Zzrrbbitt!')
# dictionary
ch.add_command({
	'name': 'DIY Descriptions',
	'format': '`!ribbot diy <item name>`',
	'trigger': 'diy',
	'function': describe_diy,
	'description': 'Will return a description of the DIY recipe.'
})
# end describe diy

# ====================
# command list
# ====================
def command_list(message, client, args):
	e = discord.Embed(title="Command List",color=color)
	for cmd in ch.commands:
		val_str = cmd['format']+': '+cmd['description']
		e.add_field(name=cmd['name'],value=val_str, inline=False)
	return message.channel.send(embed=e)
# dictionary
ch.add_command({
	'name': 'Help',
	'format': '`!ribbot help`',
	'trigger': 'help',
	'function': command_list,
	'description': 'Will return a list of commands.'
})
# end command list

client.run(token)