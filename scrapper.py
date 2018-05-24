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

	def start_scrape(self):
		self.scrape()
		self.polish_values()

	def scrape(self):
		res = req.get('https://roll20.net/compendium/dnd5e/Archmage?fromList=Archmage&Name=&Speed=#content')
		soup = bs.BeautifulSoup(res.text, 'lxml')
		temp = soup.find("h1", class_ = "page-title")
		self.name = str(temp.text)	
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

	def scrape(self):
		driver = webdriver.Firefox()
		driver.get('https://roll20.net/compendium/dnd5e/Monsters List#content')
		try:
			WebDriverWait(driver,10)
			headers = driver.find_elements_by_tag_name('a')
			for head in headers:
				print(head.text)
		finally:
			driver.quit()

#s = htmlScrapper()
#s.start_scrape()

