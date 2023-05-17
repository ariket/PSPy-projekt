import json                         #Tkinter functionality copied from https://python-forum.io/thread-39230.html
from tkinter import ttk
from tkinter import *
import tkinter as tk

 
window = tk.Tk()
window.title("V75 på lördag")
window.geometry("650x500")
 
frame1 = tk.Frame(window, bg="blue", height=300, width=700)
frame1.grid(row=1, column=0)
 
frame2 = tk.Frame(window, bg="light sky blue", height=300, width=700)
frame2.grid(row=2, column=0)
 
frame_entry = tk.Frame(frame2) #Frame para los entry
frame_entry.pack(pady=20)
 
tree_frame = tk.Frame(frame1) #Frame para el arbol
tree_frame.pack(pady=20)
 
#style del tree
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#c7c7c7", foreground="black", rowheight=25,fieldbackground="#a1a1a1")
style.map("Treeview", background=[('selected','green')])
 
tree_scroll = Scrollbar(tree_frame) #Frame para el scrollbar del arbol
tree_scroll.pack(side=RIGHT, fill=Y)
#Lista Treeview
json_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
json_tree.pack()
 
#config scroll
tree_scroll.config(command=json_tree.yview)
 
#column
json_tree['column'] = ("Lopp", "Startnummer", "Hästnamn", "Kusk", "V75 % spelad")

#column
json_tree.column("#0", width=0, minwidth=0)#Columna Fantasma
json_tree.column("Lopp", anchor="w", width=120)
json_tree.column("Startnummer", anchor="w", width=120)
json_tree.column("Hästnamn", anchor="w", width=120)
json_tree.column("Kusk", anchor="w", width=120)
json_tree.column("V75 % spelad", anchor="w", width=120)
 
#headings
json_tree.heading("#0", text="", anchor="w")#Columna Fantasma
json_tree.heading("Lopp", text="Lopp", anchor="w")
json_tree.heading("Startnummer", text="Startnummer", anchor="w")
json_tree.heading("Hästnamn", text="Hästnamn", anchor="w")
json_tree.heading("Kusk", text="Kusk", anchor="w")
json_tree.heading("V75 % spelad", text="V75 % spelad", anchor="w")

#color rows
json_tree.tag_configure('par', background="azure")

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
 
 
def select_record():
    for row in json_tree.get_children():
        json_tree.delete(row)
     
    kusk_lb.delete(0,END)
    v75_p_spelad_lb.delete(0,END)
 
    for record in data:
        #if record['race'] == 1:
        #print(Lopp_lb.get())
       #if Lopp_lb.get() == record['race'] or compare == None:
        if Lopp_lb.get():
            if int(Lopp_lb.get()) == record['race']:
                json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('par',))     
        else:
            json_tree.insert(parent='', index="end", values=(record['race'],record['startnumber'],record['name'],record['coachman'],record['v75percent']), tags=('par',)) 
    Lopp_lb.delete(0,END)
    #selected = json_tree.focus()
    #values = json_tree.item(selected,'values')    
    #Lopp_lb.insert(0, values[0]) 
    #kusk_lb.insert(0,values[2])
    #v75_p_spelad_lb.insert(0,values[3])
 
select_btn = tk.Button(frame2, text="Välj", command=select_record)
select_btn.pack(ipadx=30,)
 
#def update_record():        
#    selected = json_tree.focus()
#    datas = json_tree.item(selected, text='', values=(str(Lopp_lb.get()),,str(kusk_lb.get()),str(v75_p_spelad_lb.get()))) #guardar data
#    with open('prueba1.json', 'w',encoding="utf8") as fi:
#        json.dump({'Example': datas}, fi, indent=4)
#    Lopp_lb.delete(0,END) 
#    kusk_lb.delete(0,END)
#    v75_p_spelad_lb.delete(0,END) 
#update_btn = tk.Button(frame2, text="Update", command=update_record)
#update_btn.pack(side=RIGHT,ipadx=30, pady=10)
 
window.mainloop()