class CommandHandler:
	def __init__(self, client):
		self.client = client
		self.commands = []
	
	def add_command(self, command):
		self.commands.append(command)
	
	def command_handler(self, message):
		msg = message.content.split(" ",1)[1]
		for command in self.commands:
			if msg.startswith(command['trigger']):
				args = msg.split(' ',1)
				if( args[0] == command['trigger'] ):
					args.pop(0)
					return command['function'](message,self.client,args)
					break
				else:
					break
			else:
				break