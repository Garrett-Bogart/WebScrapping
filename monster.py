import scrapper

class monster:
	def __init__(self):
		self.name = ""
		self.AC = 0 
		self.actions = [] 
		self.alignment = ""
		self.type = ""
		self.attributes ={} 
		self.challange_rating = 0
		self.hp = ""# ex 135(18d10+36)
		self.languages = ""
		self.passivePerception = 0
		self.attacks = {}	
		self.saving_throws = {} 
		self.senses = ""	
		self.size = ""
		self.skills = {}
		self.speed = {}
		self.traits = {}
		self.type = ""
		self.legenday_actions = {}
	
	def set_values(self, name, labels, values):
		self.set_name(name)
		self.set_AC(labels,values)
		self.set_actions(labels, values)
		self.set_alignment(labels,values)
		self.set_attributes(labels,values)
		return 	

	def set_name(self, name):
		print(name)
		self.name = name
	
	def set_AC(self, labels, values):
		position = 0
		temp = ""
		for label in labels:
			if label == "AC":
				temp =values[position][0:2]
				self.AC = int(temp)
			position += 1
		print("Monster AC is: "+ str(self.AC))

	def set_actions(self, labels, values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Actions":
				temp = values[position]
				self.actions = temp
			position += 1
		self.actions = self.format_actions(temp)
		self.print_action()
		return

	def print_action(self):
		print("Actions: ")
		for dictionary in self.actions:
			print("\t"+dictionary["Name"])	
			temp = []
			for thing in dictionary:
				temp.append(thing)
			for thing in temp:
				if thing != "Name":
					print("\t\t"+thing+": "+dictionary[thing])
		return	

	def format_actions(self,stringAction):#actions is a string "[{...},{...},etc]"
		action_list = self.split_actions(stringAction)
		return self.action_dictionary(action_list)

 
	def action_dictionary(self, action):
		action_list = []
		temp = {}
		for act in action:
			part1, part2 = act.split(':')
			if part1 == 'Name':
				if temp:#if the dictionary has something append it to the list and then reset the dicitonary
					action_list.append(temp)
				temp = {}
			temp[part1] = part2
		action_list.append(temp)#catches the last dictionary
		return action_list
	
	def split_actions(self, stringAction):
		paired = 0
		temp = ""
		for char in stringAction:
			if char == "\"":
				paired+=1
				char = ""
			if char == "[" or char =="]" or char == '{' or char == '}':
				char = ""
			if paired > 1:
				paired = 0
			if char == "," and paired == 1:
				char = "*"#using * as a temporary comma so later on it can be changed back to a comma easily
			temp = temp+char
		return temp.split(',')	

	def set_alignment(self, labels, values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Alignment":
				temp =values[position]
				self.alignment = temp
			position += 1
		print("alignment is: "+ str(self.alignment))

	def set_attributes(self,labels,values):	
		position = 0
		temp = ""
		attrb = ["CHA","CON","DEX","INT","STR","WIS"]
		for label in labels:
			for att in attrb:
				if label == att:
					temp =values[position]
					self.attributes[att]=temp
			position += 1
		print(self.attributes)


	def set_traits(self, traits):
		return 
	
	def set_legendary_actions(self, actions):
		return


s = scrapper.htmlScrapper()
s.start_scrape()
m = monster()
m.set_values(s.name, s.attributeNames, s.attributeValues)

