import requests as req
import bs4 as bs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class htmlScrapper():

	def scrape(self):
		res = req.get('https://roll20.net/compendium/dnd5e/Monsters List#content')
		soup = bs.BeautifulSoup(res.text, 'lxml')
		for url in soup.find_all('a'):
			print(url.text)
		print("since the creatures are loaded in from javascript file the second h1 tag Monsters List will not appear")

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

s = htmlScrapper()
s.scrape()
print("")
print("")
s1 = javascriptScrapper()
s1.scrape()
