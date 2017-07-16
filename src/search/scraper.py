from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os 

#Current dir
dirPath = os.path.dirname(os.path.realpath(__file__))

#http://features.peta.org/cruelty-free-company-search/cruelty_free_companies_search.aspx?Dotest=8

#Function for scraping data from a page
def scrape(url):
	#list to return
	dictBrands = []
	#PhantomJS webdriver
	browser = webdriver.PhantomJS(dirPath+"/drivers/PhantomJS/bin/PhantomJS")
	#Chrome webdriver
	#browser = webdriver.Chrome(dirPath+"/drivers/chromedriver")
	browser.get(url)
	#Page soup
	soup = bs(browser.page_source, "html.parser")
	#close the browser
	browser.close()
	brands = soup.findAll("span", class_="menu")
	#Loop through array to get brands
	for el in brands:
		brand = el.text.strip()
		if "(" in brand:
			splitBrand = brand.split("(")
			newRow = {"company": splitBrand[0], "parent": splitBrand[1].strip(")")}
		else:
			newRow = {"company": brand, "parent": ""}
		dictBrands.append(newRow)
	return dictBrands