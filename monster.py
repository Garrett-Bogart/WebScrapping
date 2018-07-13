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
		self.attacks = {}#determined by actions, look for multiattack	
		self.saving_throws = {} 
		self.senses = ""	
		self.size = ""
		self.skills = {}
		self.speed = "" 
		self.traits = ""
		self.type = ""
		self.legendary_actions ="" 

	def set_values(self, name, labels, values):
		#print(labels)
		self.set_name(name)
		self.set_AC(labels,values)
		self.set_actions(labels, values)
		self.set_alignment(labels, values)
		self.set_type(labels, values)
		self.set_attributes(labels,values)
		self.set_challenge_rating(labels, values)
		self.set_hp(labels,values)
		self.set_languages(labels,values)
		self.set_passive_perception(labels, values)
		#self.set_attacks(labels,values)
		self.set_saving_throws(labels, values)
		self.set_senses(labels, values)
		self.set_size(labels, values)
		self.set_skills(labels,values)
		self.set_speed(labels,values)
		self.set_traits(labels,values)
		self.set_type(labels,values)
		self.set_legendary_actions(labels, values)
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

	def set_alignment(self,labels,values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Alignment":
				temp = values[position]
				self.alignment = temp
			position += 1
		print(self.alignment)
		return

	def set_type(self,labels,values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Type":
				temp = values[position]
				self.alignment = temp
			position += 1
		print(temp)
		return

	def set_attributes(self,labels,values):
		print(labels)
		position = 0
		for label in labels:
			if label == "STR":
				self.attributes["STR"] = int(values[position])
			if label == "DEX":
				self.attributes["DEX"] = int(values[position])
			if label == "CON":
				self.attributes["CON"] = int(values[position])
			if label == "INT":
				self.attributes["INT"] = int(values[position])
			if label == "WIS":
				self.attributes["WIS"] = int(values[position])
			if label =="CHA":
				self.attributes["CHA"] = int(values[position])
			position += 1
		print(self.attributes)
		return

	def set_challenge_rating(self,labels,values):
		position = 0
		for label in labels:
			if label =="Challenge Rating":
				self.challange_rating = values[position]
			position +=1
		print(self.challange_rating)

	def set_hp(self,labels,values):
		position = 0
		for label in labels:
			if label == "HP":
				self.hp = values[position]
			position+=1
		print("hp:"+str(self.hp))	

	def set_languages(self,labels,values):#need to add in language selection function
		position = 0
		for label in labels:
			if label == "Languages":
				self.languages = values[position]
			position+=1
		print("langauges: "+self.languages)

	def set_passive_perception(self,labels,values):
		position = 0
		for label in labels:
			if label == "Passive Perception":
				self.passivePerception = values[position]
			position+=1
		print("passive perception: "+str(self.passivePerception))

	def set_attacks(self,labels,values):
		position = 0
		for label in labels:
			if label == "Attacks":
				print(values[position])
				self.attacks["Attacks"] = values[position]
			position+=1
		print(self.attacks)

	def set_saving_throws(self, labels, values):
		position = 0
		for label in labels:
			if label == "Saving Throws":
				temp = values[position].split(",")
				for thing in temp:
					parts = thing.split("+")
					self.saving_throws[parts[0].replace(" ","")] = int(parts[1])
			position += 1
		print(self.saving_throws)

	def set_senses(self,labels, values):
		position = 0
		for label in labels:
			if label =="Senses":
				self.senses = values[position]
			position += 1
		print("senses: "+self.senses) 

	def set_size(self, labels, values):
		position = 0
		for label in labels:
			if label == "Size":
				self.size = values[position]
			position += 1
		print("size: "+ self.size)

	def set_skills(self, labels, values):
		position = 0
		for label in labels:
			if label == "Skills":
				temp = values[position].split(",")
				for thing in temp:
					parts = thing.split("+")
					self.skills[parts[0].replace(" ","")] = int(parts[1])
			position += 1
		print(self.skills)

	def set_speed(self, labels, values):# needs formating
		position = 0
		for label in labels:
			if label == "Speed":
				self.speed = values[position]
			position += 1
		print("speed: "+ self.speed)
	

	def set_traits(self, labels, values):
		position = 0
		for label in labels:
			if label == "Traits":
				self.traits = values[position]
			position+=1
		print(self.traits)
	
	def set_type(self, labels, values):
		position = 0
		for label in labels:
			if label == "Type":
				self.type = values[position]
			position+=1
		print(self.type)

	def set_legendary_actions(self, labels, values):
		position = 0
		for label in labels:
			if label == "Legendary Actions":
				self.legendary_actions = values[position]
			position += 1
		print(self.legendary_actions)


s = scrapper.htmlScrapper()
s.start_scrape()
m = monster()
m.set_values(s.name, s.attributeNames, s.attributeValues)

