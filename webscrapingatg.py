from selenium import webdriver
import time
import lxml
from bs4 import BeautifulSoup
#from bs4.diagnose import diagnose

url = "https://www.atg.se/andelsspel?sort=ranking"

webdriver = webdriver.Chrome()
webdriver.get(url)
time.sleep(2)

webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
html = BeautifulSoup(webdriver.page_source,'lxml')

