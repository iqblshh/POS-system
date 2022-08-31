'''
with open('data.txt') as data :
    for index in data :
        cont = data.readline(2)
        if cont == 'BB' :
            print("bomba")
        elif cont == 'CC' :
            print("classic")
        elif cont == 'TT' :
            print("tutut")
        else :
            print("empty space")

globals()["btn"+str(index)]

for index, new_val in enumerate(mainan) :
    print(new_val,index)


mainan = ["BB112",      # 0
          "CC191",      # 1
          "CC195",      # 2
          "TT131",      # 3
          "TT95",       # 4
          "BB103",      # 5
          "CC161",      # 6
          "TT104"]      # 7

bil = []

def semak(x) :
    bil.append(x)
    print(bil)

for x in mainan :
    semak(x)
    


from tkinter import *

root = Tk()

c = Button(root, text="a me")
c.pack()

b = Button(root, text="b me", command=lambda: b.destroy())
b.pack()

a = Button(root, text="c me", command=lambda: b.pack())
a.pack()


root.mainloop()

import tkinter as tk
 
 
root = tk.Tk()
frame = tk.Frame(root)
 
def dosomething():
    print(mylabel.config())
 
 
mylabel = tk.Label(frame, text = "Hello World", bg = "red")
mylabel.pack(padx = 5, pady = 10)
 
mybutton = tk.Button(frame, text = "Click Me", command = dosomething)
mybutton.pack(padx = 5, pady = 10)
 
 
frame.pack(padx = 5, pady = 5)
root.mainloop()

SP = {'key1': 'value1','key2': 'value2'}
CP = {'key1': 'value1','key2': 'value2'}

def test(SP,CP):
    print(SP['key1'])
    print(CP)

test(SP,CP)

senaraiMainan = {
    ############################################################
    'bomba' : {
        'jenis'     : 'BB',
        'harga'     : 15,
        'nombor'    : ['199', '192', '193', '66', '112', '192'],
    },
    ############################################################
    'skuter' : {
        'jenis'     : 'S',
        'harga'     : 15,
        'nombor'    : ['118', '128', '46', '149', '151'],
    },
 }

print(senaraiMainan['skuter']['nombor'])

import customtkinter, tkinter

app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# create scrollable textbox
tk_textbox = tkinter.Text(app, highlightthickness=0)
tk_textbox.grid(row=0, column=0, sticky="nsew")

# create CTk scrollbar
ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

# connect textbox scroll event to CTk scrollbar
tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

app.mainloop()


from tkinter import *

a = [None] * 10
i = 0
b = [None] * 10

root = Tk()

def newbut(i) :
    global b
    
    b[i] = Button(root, text=i+100, command=lambda:running())
    b[i].pack()

def running() :

    global a
    global i
    
    a[i] = Button(root, text=i, command=lambda:newbut(i))
    a[i].pack()
    i+=1

running()



root.mainloop()

myVars = vars()

myStr = 'dolu'
myStr2 = 'doku'



myVars[myStr] = 'yolo'
myVars[myStr2] = 'meggi'

print(doku)
print(dolu)

 def running(self,jenis,harga,nombor) :
        #for runIndex
        self.labelVar[nombor] = customtkinter.CTkLabel(self.frameRun, width=75, height=42, text=jenis+' '+nombor)
        self.labelVar[nombor].pack(pady=1)

        self.masukVar[nombor] = customtkinter.CTkButton(self.frameMasuk, width=75, height=42, text='Masuk', command=lambda: self.masuk(nombor))
        self.masukVar[nombor].pack(pady=1)
        
        self.cancelVar[nombor] = customtkinter.CTkButton(self.frameCancel, width=75, height=42, text='Cancel', command=lambda: self.cancel(nombor))
        self.cancelVar[nombor].pack(pady=1)

        
def masuk(self,nombor) :
        print(nombor)
        self.labelVar[nombor].destroy()
        self.masukVar[nombor].destroy()
        self.cancelVar[nombor].destroy()


    def cancel(self,nombor) :
        print(nombor)
        self.labelVar[nombor].destroy()
        self.masukVar[nombor].destroy()
        self.cancelVar[nombor].destroy()

from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Execute tkinter
root.mainloop()


senarai = {
        ############################################################
    'bomba' : {
        'nama'      : 'Bomba',
        'jenis'     : 'BB',
        'harga'     : 15,
        'nombor'    : ['199', '192', '193', '66', '112']
    },
        ############################################################
    'skuter' : {
        'nama'      : 'Skuter',
        'jenis'     : 'S',
        'harga'     : 15,
        'nombor'    : ['118', '128', '46', '149', '151']
    }
}

for k,v in senarai.items() :
    print(k,v)


x = 0
lampu = x
print(lampu == 0)
'''
# Import Module
from tkinter import *

# Create Tkinter Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Frame 1
frame1 = Frame(root,bg="black",width=500,height=300)
frame1.pack()

# Frame 2
frame2 = Frame(frame1,bg="white",width=100,height=100)
frame2.pack(pady=20,padx=20)

#Button(frame2,text='pak').pack()

# Execute Tkinter
root.mainloop()
