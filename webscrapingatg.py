from selenium import webdriver    #Selenium WebDriver is an automated testing framework used for the validation of websites (and web applications)
import time						  #The selenium package is used to automate web browser interaction from Python.
import lxml
from bs4 import BeautifulSoup     #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#from bs4.diagnose import diagnose#Web Scraping with Beautiful Soup.

#url = "https://www.atg.se/andelsspel?sort=ranking"

webdriver = webdriver.Chrome()
webdriver.get(url)
time.sleep(2)

webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
html = BeautifulSoup(webdriver.page_source,'lxml')

