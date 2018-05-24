import scrapper

class action:
	def __init__(self, blockDescription)
		self.descrption = {}

class monster:
	def __init__(self):
		self.name = ""
		self.AC = 0 
		self.actions = ""
		self.alignment = ""
		self.type = ""
		self.attributes = []
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
		print("Actions are: "+ str(self.actions))
		return
	def format_actions(self,stringAction)#actions is a string "[{...},{...},etc]"
		action_list = []
		action = {}
		sub_action = ""
		found = False
		 for char in actions:
			if char == "]":
				return action_list
			if char == "}":
				action_list.append(action)
			if char == "{":

	#returns a list of actions, actions are a dictionary
 

	def set_traits(self, traits):
		return 
	
	def set_legendary_actions(self, actions):
		return

	def set_attributes(self, attrb):
		return

s = scrapper.htmlScrapper()
s.start_scrape()
m = monster()
m.set_values(s.name, s.attributeNames, s.attributeValues)

