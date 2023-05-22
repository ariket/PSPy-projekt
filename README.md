# PSPy-projekt

Programmering och skriptning, del 1 - Python (PSPy)
Projektarbete

projektdefinition: Webscraping, alltså hämta("stjäla"/kopiera) data från en hemsida. Jag kommer ge mig på ATG.se i detta projekt.

from bs4 import BeautifulSoup	#Beautiful Soup is a Python library for pulling data out of HTML and XML files.
				#Web Scraping with Beautiful Soup.

from selenium import webdriver	#Selenium driver is an automated testing framework used for the validation of websites (and web applications).
                                #The selenium package is used to automate web browser interaction from Python.

Selenium Webdreiver fungerar bäst ihop med webläsaren Chrome, vill man absolut inte använda chrome så måste koden ändras på två ställen,
man måste då kommentera bort "driver = webdriver.Chrome()" och istället aktivera EDGE eller Firefox i kodraderna precis under.



bibliotek 	svårighetsgrad 1 	svårighetsgrad 2 	svårighetsgrad 3
BeautifulSoup	tanka ner websidor	läs av en hemsida som	läs av en hemsida och redovisa 
& webdriver				du hittat på nätet och 	data från hemsidan med tkinter
					spara filen på JSON