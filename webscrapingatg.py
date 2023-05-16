from selenium import webdriver  #Selenium driver is an automated testing framework used for the validation of websites (and web applications)
                                #The selenium package is used to automate web browser interaction from Python.
from bs4 import BeautifulSoup   #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
                                #Web Scraping with Beautiful Soup.
import time
import csv

url = "https://www.atg.se/spel/2023-05-20/V75/gavle"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

i = 0
x = 0
while i < 9:
    time.sleep(1)
    driver.execute_script(f"window.scrollTo(0, {x})")
    i +=1
    x +=500
    print(i)    

htmlRaw = BeautifulSoup(driver.page_source,'html.parser')

with open('test.csv' ,"w", newline='',encoding="utf8") as D2:
    out = csv.writer(D2) 
    for row in htmlRaw:
        out.writerow(row)

#driver.quit()
#input()