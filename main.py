import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('POS')
root.iconbitmap('C:/Users/kebaq/Documents/GitHub/POS-system/ceriatoys.ico')
root.geometry('1200x900')

mainan = ["BB112",      # 0
          "CC191",      # 1
          "CC195",      # 2
          "TT131",      # 3
          "TT95",       # 4
          "BB103",      # 5
          "CC161",      # 6
          "TT104"]      # 7


frame1 = customtkinter.CTkFrame(root, width=350, height=100)
frame1.place(x=10, y=10)

frame2 = customtkinter.CTkFrame(root, width=350, height=400)
frame2.place(x=10, y=120)
'''
frameKL = customtkinter.CTkFrame(root, width=350, height=200)
frameKL.place(x=10, y=530)

frameBB = customtkinter.CTkFrame(root, width=350, height=200)
frameBB.place(x=10, y=530)

frameCC = customtkinter.CTkFrame(root, width=350, height=200)
frameCC.place(x=10, y=530)

frameTK = customtkinter.CTkFrame(root, width=350, height=200)
frameTK.place(x=10, y=530)

frameTB = customtkinter.CTkFrame(root, width=350, height=200)
frameTB.place(x=10, y=530)

frameJS = customtkinter.CTkFrame(root, width=350, height=200)
frameJS.place(x=10, y=530)

frameAK = customtkinter.CTkFrame(root, width=350, height=200)
frameAK.place(x=10, y=530)
'''
frame3 = customtkinter.CTkFrame(root, width=350, height=200)
frame3.place(x=10, y=530)

frame4 = customtkinter.CTkFrame(root, width=150, height=720)
frame4.place(x=370, y=10)

textbox1 = customtkinter.CTkTextbox(frame1, height=50, width=200, font=("Helvetica",28))
textbox1.place(x=10, y=25)


def Bomba(bil,nama) :
    globals()["btn"+str(bil)] = customtkinter.CTkButton(frame2, text=nama)
    globals()["btn"+str(bil)].pack()

def Classic(bil,nama) :
    globals()["btn"+str(bil)] = customtkinter.CTkButton(frame2, text=nama)
    globals()["btn"+str(bil)].pack()

def Tuttut(bil,nama) :
    globals()["btn"+str(bil)] = customtkinter.CTkButton(frame2, text=nama)
    globals()["btn"+str(bil)].pack()


for index, new_val in enumerate(mainan) :

        temp = mainan[index]
        tempX = temp[0:2]

        if tempX  == 'BB' :
            Bomba(index,temp)
        elif tempX == 'CC' :
            Classic(index,temp)
        elif tempX == 'TT' :
            Tuttut(index,temp)
        else :
            print("empty space")
'''

for index, new_val in enumerate(mainan) :

        temp = mainan[index]
        tempX = temp[0:2]

        if tempX  == 'BB' :
            print(index,temp)
        elif tempX == 'CC' :
            print(index,temp)
        elif tempX == 'TT' :
            print(index,temp)
        else :
            print("empty space")
'''
#button_1 = customtkinter.CTkButton(frame1, text='Button')
#button_1button_1.pack()

#button_2 = customtkinter.CTkButton(frame1, text='Button 2')
#button_2.pack()

#button_3 = customtkinter.CTkButton(frame2, text='Button 3')
#button_3.pack()

#button_4 = customtkinter.CTkButton(frame2, text='Button 4')
#button_4.pack()

#button_5 = customtkinter.CTkButton(frame3, text='Button 5')
#button_5.pack()

root.mainloop()
