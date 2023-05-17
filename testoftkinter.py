import json                         #Tkinter functionality copied from https://python-forum.io/thread-39230.html
from tkinter import ttk
from tkinter import *
import tkinter as tk
 
ventana = tk.Tk()
ventana.title("Test")
ventana.geometry("1000x600")
 
frame1 = tk.Frame(ventana, bg="green", height=300, width=700)
frame1.grid(row=1, column=0)
 
frame2 = tk.Frame(ventana, bg="yellow", height=300, width=700)
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
json_tree['column'] = ("Lopp", "Hästnamn", "Kusk", "Something")
 
#column
json_tree.column("#0", width=0, minwidth=0)#Columna Fantasma
json_tree.column("Lopp", anchor="w", width=120)
json_tree.column("Hästnamn", anchor="w", width=120)
json_tree.column("Kusk", anchor="w", width=120)
json_tree.column("Something", anchor="w", width=120)
 
#headings
json_tree.heading("#0", text="", anchor="w")#Columna Fantasma
json_tree.heading("Lopp", text="Lopp", anchor="w")
json_tree.heading("Hästnamn", text="Hästnamn", anchor="w")
json_tree.heading("Kusk", text="Kusk", anchor="w")
json_tree.heading("Something", text="Something", anchor="w")
 
#color rows
json_tree.tag_configure('par', background="#fff")
json_tree.tag_configure('inpar', background="#d6d6d6")
 
with open('data.json', "r") as f:
    data = json.load(f)
 
 
    count=0
    for record in data:
        if count % 2 ==0:
            json_tree.insert(parent='', index="end", iid=count, text="", values=(record['race'],record['name'],record['coachman'],record['startnumber']), tags=('odds',))
        else:    
            json_tree.insert(parent='', index="end", iid=count, text="", values=(record['race'],record['name'],record['coachman'],record['startnumber']), tags=('odds',))
 
        count+=1
 
 
#entrys
l1 = Label( frame_entry, text="Lopp")
l1.grid(row=0, column=0)
Lopp_lb = Entry( frame_entry)
Lopp_lb.grid(row=1, column=0)
 
l2 = Label( frame_entry, text="Hästnamn")
l2.grid(row=0, column=1)
Hästnamn_lb = Entry(frame_entry)
Hästnamn_lb.grid(row=1, column=1)
 
l3 = Label( frame_entry, text="Kusk")
l3.grid(row=0, column=2)
lastHästnamn_lb = Entry(frame_entry)
lastHästnamn_lb.grid(row=1, column=2)
 
l4 = Label( frame_entry, text="Something")
l4.grid(row=0, column=3,)
something_lb = Entry(frame_entry)
something_lb.grid(row=1, column=3)
 
 
def select_record():
    #Limpiar las cajas
    Lopp_lb.delete(0,END) 
    Hästnamn_lb.delete(0,END)
    lastHästnamn_lb.delete(0,END)
    something_lb.delete(0,END)
 
    selected = json_tree.focus() 
    values = json_tree.item(selected,'values') 
 
    Lopp_lb.insert(0, values[0]) 
    Hästnamn_lb.insert(0,values[1])
    lastHästnamn_lb.insert(0,values[2])
    something_lb.insert(0,values[3])
 
select_btn = tk.Button(frame2, text="Select", command=select_record)
select_btn.pack(side=LEFT, ipadx=30,)
 
def update_record():        
    selected = json_tree.focus()
    data = json_tree.item(selected, text='', values=(str(Lopp_lb.get()),str(Hästnamn_lb.get()),str(lastHästnamn_lb.get()),str(something_lb.get()))) #guardar data
     
    with open('prueba1.json', 'w') as f:
        json.dump({'Example': data}, f, indent=4)
     
 
    Lopp_lb.delete(0,END) 
    Hästnamn_lb.delete(0,END)
    lastHästnamn_lb.delete(0,END)
    something_lb.delete(0,END)
 
update_btn = tk.Button(frame2, text="Update", command=update_record)
update_btn.pack(side=RIGHT,ipadx=30, pady=10)
 
ventana.mainloop()