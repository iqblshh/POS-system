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
'''
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