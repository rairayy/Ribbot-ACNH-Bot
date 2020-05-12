class CommandHandler:
	def __init__(self, client):
		self.client = client
		self.commands = []
	
	def add_command(self, command):
		self.commands.append(command)
	
	def command_handler(self, message):
		msg = message.content.split(" ",1)
		if(len(msg)>1):
			msg = msg[1]
			found = False
			for command in self.commands:
				if msg.startswith(command['trigger']):
					args = msg.split(' ',1)
					if( args[0] == command['trigger'] ):
						found = True
						args.pop(0)
						return command['function'](message,self.client,args)
						break
					else:
						break
				else:
					break
			if(not found):
				return message.channel.send('That\'s not a command. Message `!ribbit help` for the command list! Zzrrbbitt.')
		else:
			return message.channel.send('Zzrrbbitt?')