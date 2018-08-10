import scrapper
import sys
import pickle


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
		self.set_attacks(labels,values)
		self.set_saving_throws(labels, values)
		self.set_senses(labels, values)
		self.set_size(labels, values)
		self.set_skills(labels,values)
		self.set_speed(labels,values)
		self.set_traits(labels,values)
		self.set_type(labels,values)
		self.set_legendary_actions(labels, values)
	

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
		#print("Monster AC is: "+ str(self.AC))

	def remove_braces(self, action_string):
		removed_brace = action_string.replace("[","")
		removed_brace = removed_brace.replace("]","")
		removed_quotes = removed_brace.replace('"',"")
		return removed_quotes

	def single_actions(self, removed_brace):
		actions = []
		temp = ""
		for char in removed_brace:
			if char == "}":
				actions.append(temp)
				temp = ""
			else:
				if char == "{":
					continue
				temp += char
		actions = self.remove_needless_commas(actions)
		return actions
	
	def remove_needless_commas(self, actions):
		temp = []
		for action in actions:
			if action[0] == ",":
				temp.append(action.replace(",","",1))
				continue
			else:
				temp.append(action)
				continue
		return temp

	def repair_actions(self, action_parts):#occurs if action's description contain commas 
		repaired_actions = []
		for i in range(len(action_parts)):
			temp= action_parts[i].split(':')
			if len(temp) < 2:
				size = len(repaired_actions)
				patching = repaired_actions[size-1]+","+temp[0]
				repaired_actions[size-1]=patching
			else:
				repaired_actions.append(action_parts[i])
		return repaired_actions
	
	def break_actions_into_parts(self, actions):
		formatted_actions = []# {name: desc, name: desc,....}
		for action in actions:
			temp = {}
			action_parts = action.split(",")#problem if a ',' is in the desc
			repaired_actions = self.repair_actions(action_parts)
			for part in repaired_actions:
				pieces = part.split(":")
				name = pieces[0]
				desc = pieces[1]
				temp[name]=desc
			formatted_actions.append(temp)
		return formatted_actions
		
	def format_actions(self, action_string):
		removed_brace = self.remove_braces(action_string)
		actions = self.single_actions(removed_brace)
		formatted_actions = self.break_actions_into_parts(actions)
		return formatted_actions

	def get_actions(self, labels, values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Actions":
				temp = values[position]
			position += 1
		return temp

	def set_actions(self, labels, values):
		#action_string = self.read_file()
		action_string = self.get_actions(labels,values)
		self.actions = self.format_actions(action_string)
		#self.print_action(self.actions, "Actions: ")

	def print_action(self, printable, print_label):
		print(print_label)
		for dictionary in printable:
			print("\t"+dictionary["Name"])	
			temp = []
			for thing in dictionary:
				temp.append(thing)
			for thing in temp:
				if thing != "Name":
					print("\t\t"+thing+": "+dictionary[thing])


	def set_alignment(self,labels,values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Alignment":
				temp = values[position]
				self.alignment = temp
			position += 1
		#print(self.alignment)
		return

	def set_type(self,labels,values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Type":
				temp = values[position]
				self.type = temp
			position += 1
		#print("Type: "+self.type)
		return

	def set_attributes(self,labels,values):
		#print(labels)
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
		#print(self.attributes)
		return

	def set_challenge_rating(self,labels,values):
		position = 0
		for label in labels:
			if label =="Challenge Rating":
				self.challange_rating = values[position]
			position +=1
		#print(self.challange_rating)

	def set_hp(self,labels,values):
		position = 0
		for label in labels:
			if label == "HP":
				self.hp = values[position]
			position+=1
		#print("hp:"+str(self.hp))	

	def set_languages(self,labels,values):#need to add in language selection function
		position = 0
		for label in labels:
			if label == "Languages":
				self.languages = values[position]
			position+=1
		#print("langauges: "+self.languages)

	def set_passive_perception(self,labels,values):
		position = 0
		for label in labels:
			if label == "Passive Perception":
				self.passivePerception = values[position]
			position+=1
		#print("passive perception: "+str(self.passivePerception))

	def set_attacks(self,labels,values):
		position = 0
		for label in labels:
			if label == "Attacks":
				print(values[position])
				self.attacks["Attacks"] = values[position]
			position+=1
		#print(self.attacks)

	def set_saving_throws(self, labels, values):
		position = 0
		for label in labels:
			if label == "Saving Throws":
				temp = values[position].split(",")
				for thing in temp:
					parts = thing.split("+")
					self.saving_throws[parts[0].replace(" ","")] = int(parts[1])
			position += 1
		#print(self.saving_throws)

	def set_senses(self,labels, values):
		position = 0
		for label in labels:
			if label =="Senses":
				self.senses = values[position]
			position += 1
		#print("senses: "+self.senses) 

	def set_size(self, labels, values):
		position = 0
		for label in labels:
			if label == "Size":
				self.size = values[position]
			position += 1
		#print("size: "+ self.size)

	def set_skills(self, labels, values):
		position = 0
		for label in labels:
			if label == "Skills":
				temp = values[position].split(",")
				for thing in temp:
					parts = thing.split("+")
					self.skills[parts[0].replace(" ","")] = int(parts[1])
			position += 1
		#print(self.skills)

	def set_speed(self, labels, values):# needs formating
		position = 0
		for label in labels:
			if label == "Speed":
				self.speed = values[position]
			position += 1
		#print("speed: "+ self.speed)
	

	def set_traits(self, labels, values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Traits":
				temp = values[position]
				self.traits = self.format_actions(temp)
				#self.print_action(self.traits, "Traits: ")	
			position+=1
		
	def set_type(self, labels, values):
		position = 0
		for label in labels:
			if label == "Type":
				self.type = values[position]
			position+=1
		#print(self.type)

	def set_legendary_actions(self, labels, values):
		position = 0
		temp = ""
		for label in labels:
			if label == "Legendary Actions":
				temp = values[position]
				self.legendary_actions = self.format_actions(temp)
				#self.print_action(self.legendary_actions, "Legendary Actions: ")
			position+=1
def main():
	success = True
	loaded = False
	monster_guide =[]
	try:
		open_file = open('pickled_monsters.pickle', 'rb')
		monster_guide = pickle.load(open_file)
		loaded = True
	except:
		print("Failed to load pickled monsters")
	else:
		open_file.close()

	if loaded == False:
		j = scrapper.javascriptScrapper()
		j.scrape()
		s = scrapper.htmlScrapper()
		print(len(j.links))
		for i in range(len(j.links)):
			try:
				s.start_scrape(j.links[i])
				m = monster()
				m.set_values(s.name, s.attributeNames, s.attributeValues)
				monster_guide.append(m)
			except:
				print("Failed: {}".format(j.links[i]))
				success = False
		print(len(monster_guide))

	if success == True and loaded == False:
		try:
			new_file = open('pickled_monsters.pickle', 'wb')
			pickle.dump(monster_guide, new_file)
		except:
			print("Failed to pickle the object")
			raise
		else:
			new_file.close()
	print("Monster Guide is completed")
	counter = 0
	for monster in monster_guide:
		print(monster.name)
		counter+=1
	print("Monster Guide contains: {}".format(counter))

main()


