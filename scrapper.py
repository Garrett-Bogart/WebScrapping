import requests as req
import bs4 as bs
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class htmlScrapper():
	def __init__(self):
		self.name = ""
		self.attributeNames = []
		self.attributeValues = []

	def start_scrape(self, link):
		self.scrape(link)
		self.polish_values()

	def scrape(self,link):
		res = req.get(link)
		soup = bs.BeautifulSoup(res.text, 'lxml')
		temp = soup.find("h1", class_ = "page-title")
		self.name = temp.text	
		self.attributeValues = soup.find_all("div", class_ = "col-md-7 attrValue")
		self.attributeNames = soup.find_all("div", class_ = "col-md-3 attrName")

	def polish_values(self):
		#print("polishing")
		polishedValues = []
		polishedNames = []
		for i in range(len(self.attributeNames)):
			nameText =""+self.attributeNames[i].text
			temp = ""+self.attributeValues[i].text
			valueText = temp[:len(temp)//2]
			polishedNames.append(nameText)
			polishedValues.append(valueText)
		self.attributeNames = polishedNames
		self.attributeValues = polishedValues
		self.strip_whitespace()
		#print("Name:"+ self.name)
		#print("_______________________________________________")
		#for i in range(len(self.attributeValues)):
			#print(self.attributeNames[i]+": "+self.attributeValues[i])
			#print("_____________________________________________________")
		return

	def strip_whitespace(self):
		temp = []
		for text in self.attributeValues:
			text=text.strip()
			temp.append(text)
		self.attributeValues = temp
		return

class javascriptScrapper():

	def __init__(self):
		self.footer= re.compile(r'Acknowledgements|5th Edition SRD|View All Rules .|Terms of Service & Privacy Policy|DMCA|Visit our FAQ.|Home|Menu|Rules')
		self.whiteSpace = re.compile(r'[^\s]')
		self.links = []
		self.names = []
	def scrape(self):
		driver = webdriver.Firefox()
		driver.get('https://roll20.net/compendium/dnd5e/Monsters List#content')
		try:
			WebDriverWait(driver,5)
			headers = driver.find_elements_by_tag_name('a')
			for head in headers:
				if re.match(self.footer,head.text)== None and re.match(self.whiteSpace, head.text) != None:
					self.names.append(head.text)
					continue
		#	print("names gathered")
		#	print(self.names)
			self.link_maker()
		#	print("links made")
		#	print(len(self.links))
		finally:
			driver.quit()

	def link_maker(self):
		print("making links")
		for name in self.names:
		#	print(type(name))
			new = name.replace(" ",'%20')
			self.links.append('https://roll20.net/compendium/dnd5e/'+new+'?fromList='+new+'&Name=&Speed=#content')

#j = javascriptScrapper()
#j.scrape()
#s = htmlScrapper()
#s.start_scrape()

