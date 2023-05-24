#Webscraping app. Used for extracting data from websites, this program will fetch data from ATG.se
from selenium import webdriver  #Selenium driver is an automated testing framework used for the validation of websites (and web applications)
                                #The selenium package is used to automate web browser interaction from Python.
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup   #Beautiful Soup is a Python library for pulling data out of HTML and XML files.
                                #Web Scraping with Beautiful Soup.
import time
import csv
import json
from tkinter import ttk
from tkinter import *
import tkinter as tk
import random
from enum import Enum
import operator

class Horse:
    def __init__(self, name , race = 0, coachman = "", startnumber = 0 , odds = 0, v75percent = 0):
        self.name = name
        self.race = race
        self.coachman = coachman
        self.startnumber = startnumber
        self.odds = odds
        self.v75percent = v75percent
    def replace(self,new):        
        self.name = new.name
        self.race = new.race
        self.coachman = new.coachman
        self.startnumber = new.startnumber
        self.odds = new.odds
        self.v75percent = new.v75percent

class NumOfhorses(Enum): #Number of horses per race with AriBoy 108
    oneHorse = 2
    twoHorses = 2
    threeHorses = 3

#My own AriBoy 108(Harry Boy), number of horses to chose for a raceday: 1,1,2,2,3,3,3         
def AriBoy():        
    R1 = [];R2 = [];R3 = [];R4 = [];R5 = [];R6 = [];R7 = []; RR =[]
    Favhorse1 = Horse("TEMP1"); Favhorse2 = Horse("TEMP2"); Favhorse3 = Horse("TEMP3")

    def PrintHorse(Race):
        for horse in Race:
            print(f"{horse.startnumber:5}  {horse.name:25} ")

    def SortHorse(num,Race):
        while len(Race) > num:      
            delete = True
            while delete:
                numb = random.randint(1,15)
                for horse in Race:
                    if "STRUKEN-" == horse.name[:8]:
                        Race.remove(horse)
                        delete = False
                        break
                    if horse.startnumber == numb:
                        numbb = random.randint(1,10)
                        if horse.v75percent > 19 and numbb < 4: #30 % random chance
                            Race.remove(horse)
                            delete = False
                            break
                        elif horse.v75percent > 14 and numbb < 5: #40 % random chance
                            Race.remove(horse)
                            delete = False
                            break
                        elif horse.v75percent > 8 and numbb < 6: #50 % random chance
                            Race.remove(horse)
                            delete = False
                            break
                        elif horse.v75percent <= 8 and numbb < 8: #70 % random chance
                            Race.remove(horse)
                            delete = False
                            break
                        
    def Favhorse(race):
        race.sort(reverse=True,key=operator.attrgetter("v75percent"))
        for horse in race:
            if Favhorse1.race == horse.race:
                num = random.randint(1,8)
                if num < 8:   #88% random possibility
                    horse.replace(Favhorse1)
                break
            elif Favhorse2.race == horse.race:
                num = random.randint(1,5)
                if num < 5:   #80% random possibility
                    horse.replace(Favhorse2)
                break
            elif Favhorse3.race == horse.race:
                num = random.randint(1,4)
                if num < 4:   #75% random possibility
                    horse.replace(Favhorse3)    
                break
        race.sort(reverse=False,key=operator.attrgetter("startnumber"))
        
    with open('data.json',encoding="utf8") as data_file:    
        data = json.load(data_file)    
    for horse in data:
        if Favhorse1.v75percent < horse["v75percent"]:  #pick out the 3 horses with highest v75percent
            Favhorse3.replace(Favhorse2)
            Favhorse2.replace(Favhorse1)
            Favhorse1 = Horse(**horse)
        elif Favhorse2.v75percent < horse["v75percent"]:
            Favhorse3.replace(Favhorse2)
            Favhorse2 = Horse(**horse)
        elif Favhorse3.v75percent < horse["v75percent"]:
            Favhorse3 = Horse(**horse)
        else:
            pass
        if int(horse['race']) == 1 and horse["v75percent"] > 5:  #only pick out horses that are palyed over this percent
            R1.append(Horse(**horse))
        if int(horse['race']) == 2 and horse["v75percent"] > 4:
            R2.append(Horse(**horse))
        if int(horse['race']) == 3 and horse["v75percent"] > 5:
            R3.append(Horse(**horse))
        if int(horse['race']) == 4 and horse["v75percent"] > 4:
            R4.append(Horse(**horse))
        if int(horse['race']) == 5 and horse["v75percent"] > 2: 
            R5.append(Horse(**horse))
        if int(horse['race']) == 6 and horse["v75percent"] > 5:
            R6.append(Horse(**horse))
        if int(horse['race']) == 7 and horse["v75percent"] > 4:
            R7.append(Horse(**horse))    
    
    num1 = 0; num2 = 0; num3 = 0 #Variables to get right number of horses a race
    RR = R1; numRR = 1; rowSorted = False
    while numRR < 8: # 7 Races to sort out variable RR used temporarily when calling functions
        if rowSorted:
            rowSorted = False
            numRR += 1  
            if numRR == 2:
                R1 = RR
                RR = R2
            elif numRR == 3:
                R2 = RR 
                RR = R3    
            elif numRR == 4:
                R3 = RR
                RR = R4
            elif numRR == 5:
                R4 = RR
                RR = R5     
            elif numRR == 6:
                R5 = RR
                RR = R6
            elif numRR == 7:
                R6 = RR
                RR = R7        
        
        num = random.randint(1,3)         
        if num == 1 and num1 < NumOfhorses.oneHorse.value:
            num1 += 1
            SortHorse(1,RR)
            Favhorse(RR)
            rowSorted = True
        elif num == 2 and num2 < NumOfhorses.twoHorses.value:
            num2 += 1
            SortHorse(2,RR)
            Favhorse(RR)
            rowSorted = True
        else:
            if num3 < NumOfhorses.threeHorses.value:
                num3 += 1
                SortHorse(3,RR)
                Favhorse(RR)
                rowSorted = True
    print("Veckans slumpvis utvalda AriBoy 108 rader")
    print("-------------------------------")
    PrintHorse(R1)
    print("-------------------------------")
    PrintHorse(R2)
    print("-------------------------------")
    PrintHorse(R3)
    print("-------------------------------")
    PrintHorse(R4)
    print("-------------------------------")
    PrintHorse(R5)
    print("-------------------------------")
    PrintHorse(R6)
    print("-------------------------------")
    PrintHorse(R7)
    print("-------------------------------")
    
def ScrapeSorting():        
    row=0 ; rightRow = False
    list = [] #Holds all relevant data, unsorted, 
#Only uses the line starts with: ""/></div><span class=""MuiTouchRipple-root horse-w0pj6f""></span></button><div style=""position: relative;""""
#This line is line 903 for the moment, if that changes the code must also be changed at "if row == 903:" 
    with open('temp.csv','r',encoding="utf8") as file:
        for line in file:
            row += 1
            #if row == 903:
            if line[10:64] == """/></div><span class=""MuiTouchRipple-root horse-w0pj6f""": 
                rightRow = True   #print("Hittade rätt rad")
                for blocks in line.split("""class=""horse-name css-2oi2tb-horseview-styles--horseName"">"""):  
                    list.append(blocks)
    list.pop(0) #delete first item in list, no useful data

    horse = [] #All horses of the weeks v75 are saved in this list.
    race = 1
    startnumb = "1"
    for post in list:    #Sorting out useful data from scraped raw-data
        name = post.replace("<span>", "</span>").split("</span>")
        if name[2][44:58] == "changed-driver":  #special handle if coachdriver are changed
            name[2] = name[2][85:]
            special = name[2].split(""""">""")
            name[4] = name[3]
            name[3] = special[1]
        odds = name[4].replace("</td><td","""-col"">""").split("""-col"">""")
        if odds[4] == "EJ":                 #Drawn horse
            name[0] = "STRUKEN-" + name[0]    
        odds[2] = odds[2][:-1]
        horse.append(Horse(name[0], race, name[3], int(startnumb) , odds[4], int(odds[2])))

        head = post.split("startlist-button-leg-")
        try:
            race = int(head[1][0])
            startnumb = head[1][8:10]
            if startnumb[1] == "\u0022":
                startnumb = head[1][8:9]
        except:
            pass  
    with open('data.json','w',encoding="utf8") as jsf:     #Save all useful data to json file
        json.dump([obj.__dict__ for obj in horse], jsf, indent=4)        
    if rightRow:
        print("\nSorteringen är nu genomförd\n")
    else:
        print("\nSorteringen har troligen misslyckats, kontrollera i koden(rad 189) att programmet hittar rätt rad\n")

def ScrapeAtg():
    print("Nu börjar skrapningen av atg.se/spel/V75 \nAvvakta, det tar ca 15 sekunder....")
    url = "https://www.atg.se/spel/V75/"
    #url = "https://www.atg.se/spel/2023-05-20/V75/gavle"
    driver = webdriver.Chrome()  #NYI user may not have Chrome installed 
    #driver = webdriver.Edge() #Try this if you only have edge installed on your computer
    #driver = webdriver.Firefox() #Try this if you only have firefox installed on your computer
    driver.get(url)
    time.sleep(3)

    x = 0 ; i = 0
    while i < 10:     #Scroll down to bottom of webpage to be able to scrape all data
        time.sleep(1)
        driver.execute_script(f"window.scrollTo(0, {x})")
        i +=1
        x +=500
        print(i)    

    htmlRaw = BeautifulSoup(driver.page_source,'html.parser') #Load whole webpage to htmlRaw
    with open('temp.csv' ,"w", newline='',encoding="utf8") as D2: #Save all data to a file
        out = csv.writer(D2) 
        for row in htmlRaw:
            out.writerow(row)
    driver.quit()
    print("Skrapningen av atg.se/spel/V75 är nu slutförd\n")
    print("Allt verkar ha gått bra\n") #NYI gör kontroll att allt verkligen gått bra
    
def ShowTkinter():           #Tkinter functionality copied from https://python-forum.io/thread-39230.html
    window = tk.Tk()
    window.title("V75 på lördag")
    window.geometry("650x500")
 
    frame1 = tk.Frame(window, bg="blue", height=300, width=700)
    frame1.grid(row=1, column=0)
    frame2 = tk.Frame(window, bg="light sky blue", height=300, width=700)
    frame2.grid(row=2, column=0)
    frame_entry = tk.Frame(frame2) 
    frame_entry.pack(pady=20)
    tree_frame = tk.Frame(frame1) 
    tree_frame.pack(pady=20)
 
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#c7c7c7", foreground="black", rowheight=25,fieldbackground="#a1a1a1")
    style.map("Treeview", background=[('selected','blue')])
 
    tree_scroll = Scrollbar(tree_frame) 
    tree_scroll.pack(side=RIGHT, fill=Y)
    #List Treeview
    json_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    json_tree.pack()
 
    #config scroll
    tree_scroll.config(command=json_tree.yview)
 
    #column
    json_tree['column'] = ("Lopp", "Startnummer", "Hästnamn", "Kusk", "V75 % spelad")
    json_tree.column("#0", width=0, minwidth=0)#Columna Fantasma
    json_tree.column("Lopp", anchor="w", width=40)
    json_tree.column("Startnummer", anchor="w", width=80)
    json_tree.column("Hästnamn", anchor="w", width=160)
    json_tree.column("Kusk", anchor="w", width=140)
    json_tree.column("V75 % spelad", anchor="w", width=100)
 
    #headings
    json_tree.heading("#0", text="", anchor="w")#Columna Fantasma
    json_tree.heading("Lopp", text="Lopp", anchor="w")
    json_tree.heading("Startnummer", text="Startnummer", anchor="w")
    json_tree.heading("Hästnamn", text="Hästnamn", anchor="w")
    json_tree.heading("Kusk", text="Kusk", anchor="w")
    json_tree.heading("V75 % spelad", text="V75 % spelad", anchor="w")

    #color rows
    json_tree.tag_configure('par', background="azure")
    json_tree.tag_configure('pars', background="DeepSky Blue2")

    with open('data.json', "r",encoding="utf8") as f:
        data = json.load(f)
        for record in data:
            json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('par',)) 
 
    #entrys
    l1 = Label( frame_entry, text="Lopp")
    l1.grid(row=0, column=0)
    Lopp_lb = Entry( frame_entry)
    Lopp_lb.grid(row=1, column=0)
    
    l3 = Label( frame_entry, text="Kusk")
    l3.grid(row=0, column=1)
    kusk_lb = Entry(frame_entry)
    kusk_lb.grid(row=1, column=1)
 
    l4 = Label( frame_entry, text="V75 % spelad")
    l4.grid(row=0, column=2,)
    v75_p_spelad_lb = Entry(frame_entry)
    v75_p_spelad_lb.grid(row=1, column=2)

    def SelectRecord():
        for row in json_tree.get_children():
            json_tree.delete(row)
        for record in data:
            if Lopp_lb.get():
                if int(Lopp_lb.get()) == record['race']:
                    json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('pars',))     
            elif kusk_lb.get():
                if kusk_lb.get() == record['coachman']:
                    json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('pars',))     
            elif v75_p_spelad_lb.get():
                if int(v75_p_spelad_lb.get()) <= int(record['v75percent']):
                    json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('pars',))     
            else:
                json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('par',)) 
        Lopp_lb.delete(0,END)
        kusk_lb.delete(0,END)
        v75_p_spelad_lb.delete(0,END)    

    def OpenClicked():
        #item_index = json_tree.index(json_tree.focus())
        item_details = json_tree.item(json_tree.focus())
        #values = item_details.get("values")
        values = item_details.get("values")
        del values[0] ; del values[0]; del values[1]; del values[1]
        print(f"Öppnar info om {values}\nSidan stängs automatiskt efter 20 sekunder")
        #print(values[2])
        #print(item_details.get("values")[2])
        driver = webdriver.Chrome()            #NYI user may not have Chrome installed
        #driver = webdriver.Edge() #Try this if you only have edge installed on your computer
        #driver = webdriver.Firefox() #Try this if you only have firefox installed on your computer
        driver.get("https://www.breedly.com/search-horse")
        putinfo = driver.find_element(By.ID,"react-select-horse-search-input")
        putinfo.click()
        putinfo.send_keys(values)
        #putinfo.send_keys(item_details.get("values")[2])
        putinfo.click()
        time.sleep(20)
        
    select_btn = tk.Button(frame2, text="Välj", command=SelectRecord)
    select_btn.pack(ipadx=30,)
    
    go_btn = tk.Button(frame1, text="Horse info", command=OpenClicked)
    go_btn.pack(ipadx=30,)
    window.mainloop()

def Help():
    print("-----------------------------------------------------------------")
    print("<skrapa>         - Skrapa en Websida  ")
    print("<sortera>        - Sorterar ut intressant data från det skrapade")
    print("<visa>           - Visar sorterad data")
    print("<sluta>          - För att sluta  ")
    print("<ab>             - Förslag på tipsrad att lämna in för veckans v75")
    print("------------------------------------------------------------------")

while(True):
    command = input("Kommando: ").split()
    if command[0] == "skrapa":
        ScrapeAtg()
    elif command[0] == "sortera":
        ScrapeSorting()
    elif command[0] == "visa":
        ShowTkinter()    
    elif command[0] == "hjälp":
        Help()
    elif command[0] == "AB" or command[0] == "ab" : 
        print("\033[1;31m ---AriBoy--- \033[0m\n")
        AriBoy()
    elif command[0] == "sluta" or command[0] == "quit" or command[0] == "q" or command[0] == "x":
        break
    else:
        print(f"{command[0]} är ett okänt kommando") 
        Help()
