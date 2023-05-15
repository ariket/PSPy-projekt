from selenium import webdriver    #Selenium driver is an automated testing framework used for the validation of websites (and web applications)
                                  #The selenium package is used to automate web browser interaction from Python.
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup     #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
#from bs4.diagnose import diagnose#Web Scraping with Beautiful Soup.
import json
import csv
import time

#url = "https://www.atg.se/spel/2023-05-20/V75/gavle"
#url = "https://www.atg.se/andelsspel?sort=ranking"
url = "https://www.atg.se/andelsspel?gameIds=V64_2023-05-18_7_5&maxShareCost=1000&sort=ranking&ordering=desc"
#url = "http://www.begagnade-bilar.se/Search.aspx?keywords=bmw"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(7)
driver.implicitly_wait(1)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
i = 0
x = 1000
while i < 10:
    time.sleep(1)
    driver.execute_script(f"window.scrollTo(0, {x})")
    i +=1
    x +=1000
    print(i)
    
driver.implicitly_wait(1)
html = BeautifulSoup(driver.page_source,'html.parser')

with open('test.csv' ,"w", newline='',encoding="utf8") as D2:
    #out = csv.writer(D2, delimiter=',', quotechar='"')
    out = csv.writer(D2) 
    for row in html:
        out.writerow(row)

#with open("test.json", "w") as outfile:
#    json.dump(html, outfile, indent=4, ensure_ascii=False) 
"""
while True:
    # do stuff on the page
    try:
        next = driver.find_element(By.LINK_TEXT,"Nästa >>")
        if next:
            next.click()
        else:
            break
    except:
        pass
"""        
        


#driver.quit()
#input()