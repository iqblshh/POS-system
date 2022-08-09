import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('POS')
root.iconbitmap('C:/Users/kebaq/Documents/GitHub/POS-system/ceriatoys.ico')
root.geometry('500x500')

def Bomba() :
    print('bomba')

def Classic() :
    print('classic')

def Tuttut() :
    print('tuttut')

with open('data.txt') as data :
    i = 0
    for x in data :
        i+=1
        contents = data.readline(2)
        if contents == 'BB' :
            Bomba()
        elif contents == 'CC' :
            Classic()
        elif contents == 'TT' :
            Tuttut()
        print(i)

button_1 = customtkinter.CTkButton(root, text='Button')
button_1.grid(column=0, row=0)

button_2 = customtkinter.CTkButton(root, text='Button 2')
button_2.grid(column=1, row=0)

button_3 = customtkinter.CTkButton(root, text='Button 3')
button_3.grid(column=1, row=1)

button_4 = customtkinter.CTkButton(root, text='Button 4')
button_4.grid(column=2, row=0)

button_5 = customtkinter.CTkButton(root, text='Button 5')
button_5.grid(column=0, row=2)

root.mainloop()
