import csv

class Horse:
    def __init__(self, name , race = 0, coachman = "", startnumber = 0, odds = 0, v75percent = 0):
        self.name = name
        self.race = race
        self.coachman = coachman
        self.startnumber = startnumber
        self.odds = odds
        self.v75percent = v75percent
X=0
list = [] #Holds all relevant data, unsorted, 
#Only use line 903 from file, the line starts with: ""/></div><span class=""MuiTouchRipple-root horse-w0pj6f""></span></button><div style=""position: relative;""""
with open('test.csv','r',encoding="utf8") as f:
    for line in f:
        X += 1
        if X == 903:
            for blocks in line.split("""class=""horse-name css-2oi2tb-horseview-styles--horseName"">"""):  
                list.append(blocks)
list.pop(0) #delete first item in list, no useful data
horse = []
race = 1
startnumber = 1
for post in list:
    name = post.replace("<span>", "</span>").split("</span>")
    odds = name[4].replace("</td><td","""-col"">""").split("""-col"">""")
    horse.append(Horse(name[0],race, name[3],startnumber ,odds[4], odds[2]))

    head = post.split("startlist-button-leg-")
    try:
        race = head[1][0]
        startnumber = head[1][8:10]
        if startnumber[1] == u"\u0022":
            startnumber = head[1][8:9]
    except:
        pass