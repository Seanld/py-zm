# Python-based interpreter for Z- programs.

import sys

LITERAL_TYPES = {
	"flt": float,
	"str": str,
	"int": int,
	"arr": list
}
		
class Interpreter (object):
	def __init__(self, source):
		self.plain = source
		self.VARIABLES = {}
		self.FUNCTIONS = {}
		self.parse()
		
	def write(self, text):
		self.abstracted += text
		
	def convertVars(self, string): # Looks through string and converts any variable reference to it's value as a string as well.
		converted = string
		VARIABLE_NAMES = self.VARIABLES.keys()
		for name in VARIABLE_NAMES:
			if "@"+name in converted:
				converted = converted.replace("@"+name, str(self.VARIABLES[name]))
		return converted
		
	def execute(self, line, function=False):
		global individuals
		individuals = None
		blockeds = []
		if function: # We are running the content of a function
			individuals = line.split("; ")
			for item in individuals:
				blockeds.append(item.split(" "))
		else:
			global blocked
			blocked = line.split(" ")
		action = blocked[0]
		if individuals is not None: ##### PARSE FUNCTION CODE #####
			blockedsindex = 0
			for subline in individuals:
				blocked = blockeds[blockedsindex]
				action = blocked[0]
				if "*" in action[0] and ":" == action[1]: # Is a built-in function call
					pass
				elif "*" == action[0]: # Is a built-in variable call
					pass
				elif ":" == action[0]: # Is a user-defined function call (not yet nestable in functions)
					pass
				else: # Check for keyword
					if action == "set": # Create a new variable
						name = blocked[2]
						if ":" == name[-1]: # Defining a new function
							return_type = blocked[1] # This shows what the function is supposed to return at the end of it's runtime
							trail_width = 6+len(return_type)+len(name)
							afterwards = subline[trail_width:]
							self.FUNCTIONS[name[:-1]] = {"return_type": return_type, "content": afterwards}
						else: # Define new variable/literal
							literal_type = LITERAL_TYPES[blocked[1]]
							if literal_type == str or literal_type == list: # If variable type requires rest of line
								trail_width = 8+len(blocked[1])+len(name)
								afterwards = subline[trail_width:]
								if literal_type == list:
									value = afterwards.split(", ")
								elif literal_type == str:
									value = afterwards
							else: # Otherwise just get last block for simplicity
								value = literal_type(blocked[4])
							self.VARIABLES[name] = value
							
					elif action == "make": # Create a new function
						pass
						
					elif action == "print:": # Print statement
						trail_width = 7
						toPrint = self.convertVars(subline[trail_width:])
						print(toPrint)
				
				blockedsindex += 1
		elif individuals is None: ##### PARSE NORMAL LINE #####
			if "*" in action[0] and ":" == action[1]: # Is a built-in function call
				pass
			elif "*" == action[0]: # Is a built-in variable call
				pass
			elif ":" == action[0]: # Is a user-defined function call
				function_name = action[1:]
				content = self.FUNCTIONS[function_name]["content"]
				self.execute(content, function=True)
			else: # Check for keyword
				if action == "set": # Create a new variable
					name = blocked[2]
					if ":" == name[-1]: # Defining a new function
						return_type = blocked[1] # This shows what the function is supposed to return at the end of it's runtime
						trail_width = 6+len(return_type)+len(name)
						afterwards = line[trail_width:]
						self.FUNCTIONS[name[:-1]] = {"return_type": return_type, "content": afterwards}
					else: # Define new variable/literal
						literal_type = LITERAL_TYPES[blocked[1]]
						if literal_type == str or literal_type == list: # If variable type requires rest of line
							trail_width = 8+len(blocked[1])+len(name)
							afterwards = line[trail_width:]
							if literal_type == list:
								value = self.convertVars(afterwards).split(", ")
							elif literal_type == str:
								value = self.convertVars(afterwards)
						else: # Otherwise just get last block for simplicity
							value = literal_type(self.convertVars(blocked[4]))
						self.VARIABLES[name] = value
						
				elif action == "make": # Create a new function
					pass
					
				elif action == "print:":
					trail_width = 7
					toPrint = self.convertVars(line[trail_width:])
					print(toPrint)
		
	def parse(self):
		for line in self.plain.splitlines(): # iterate lines
			if line != "" and line[0:2] != "//": # Isn't empty or a comment line
				self.execute(line)

opened = open(sys.argv[1], "r")
content = opened.read()
opened.close()
zterp = Interpreter(content)
