import csv
    
X=0
list = [] #Holds all relevant data, unsorted, 
#Only use line 903 from file, the line starts with: ""/></div><span class=""MuiTouchRipple-root horse-w0pj6f""></span></button><div style=""position: relative;""""
with open('test.csv','r',encoding="utf8") as f:
    for line in f:
        X += 1
        if X == 903:
            for blocks in line.split("""class=""horse-name css-2oi2tb-horseview-styles--horseName"">"""):  
                list.append(blocks)
list.pop(0) #delete first item in list
horse = []
for post in list:
    name = post.split("</span>")
    horse.append(name[0])