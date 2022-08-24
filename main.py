'''
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('POS')
root.iconbitmap('C:/Users/kebaq/Documents/GitHub/POS-system/ceriatoys.ico')
root.geometry('1200x900')
root.minsize(1200,900)
root.maxsize(1200,900)

############################################################

frame1 = customtkinter.CTkFrame(root, width=350, height=100)
frame1.place(x=10, y=10)

frame2 = customtkinter.CTkFrame(root, width=350, height=400)
frame2.place(x=10, y=120)

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

frame3 = customtkinter.CTkFrame(root, width=350, height=200)
frame3.place(x=10, y=530)

frame4 = customtkinter.CTkFrame(root, width=150, height=720)
frame4.place(x=370, y=10)

textbox1 = tkinter.Text(frame1, height=1, width=3, bg='gray19', font=("Helvetica",25))
textbox1.place(x=10, y=25)

############################################################

mainan = ["BB112",      # 0
          "CC191",      # 1
          "CC195",      # 2
          "TT131",      # 3
          "TT95",       # 4
          "BB103",      # 5
          "CC161",      # 6
          "TT104"]      # 7

bb = []
bbIndex = 0

cc = []
ccIndex = 0

tt = []
ttIndex = 0

############################################################

def Bomba(nama) :
    global bbIndex
    bb.append(nama)
    bb[bbIndex] = customtkinter.CTkButton(frame2, text=nama)
    bb[bbIndex].pack()
    bbIndex+=1

def Classic(nama) :
    global ccIndex
    cc.append(nama)
    cc[ccIndex] = customtkinter.CTkButton(frame2, text=nama)
    cc[ccIndex].pack()
    print(cc[ccIndex])
    ccIndex+=1

def Tuttut(nama) :
    global ttIndex
    tt.append(nama)
    tt[ttIndex] = customtkinter.CTkButton(frame2, text=nama)
    tt[ttIndex].pack()
    ttIndex+=1


for nama in mainan :

        temp = nama[0:2]

        if temp == 'BB' :
            Bomba(nama)
        elif temp == 'CC' :
            Classic(nama)
        elif temp == 'TT' :
            Tuttut(nama)
        else :
            print("empty space")




############################################################





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
'''

import tkinter
from turtle import width
from typing import Text
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

############################################################
bomba = {
    "jenis"     : "BB"
    "harga"     : 15
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
kepalaLori = {
    "jenis"     : "KL"
    "harga"     : 15
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
classic = {
    "jenis"     : "CC"
    "harga"     : 20
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
tututKecik = {
    "jenis"     : "TK"
    "harga"     : 25
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
tututBesaq = {
    "jenis"     : "TB"
    "harga"     : 30
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
aima = {
    "jenis"     : "A"
    "harga"     : 20
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
atvKecik = {
    "jenis"     : "AK"
    "harga"     : 20
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
atvBesaq = {
    "jenis"     : "AB"
    "harga"     : 25
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
jetski = {
    "jenis"     : "JS"
    "harga"     : 20
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
beam = {
    "jenis"     : "B"
    "harga"     : 20
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################
princess = {
    "jenis"     : "PC"
    "harga"     : 25
    "nombor"    : ["199", "192", "193", "66", "112", "192"]
}
############################################################


class Pos :

    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title('POS')
        self.root.iconbitmap('C:/Users/kebaq/Documents/GitHub/POS-system/ceriatoys.ico')
        self.root.geometry('1200x900')
        self.root.minsize(1200,900)
        self.root.maxsize(1200,900)

        self.frameEntry = customtkinter.CTkFrame(self.root, width=200, height=100)
        self.frameEntry.place(x=10, y=10)

        self.entry1 = customtkinter.CTkEntry(self.frameEntry, width=95, height=70, text_font=("Helvetica",25), justify='center')
        self.entry1.place(x=10, y=15)
        
        self.buttonEntry = customtkinter.CTkButton(self.frameEntry, width=75, height=42, text="OK")
        self.buttonEntry.place(x=115, y=29)

        self.frameMainan = customtkinter.CTkFrame(self.root, width=770, height=770)
        self.frameMainan.place(x=10, y=120)

        self.frameMasuk = customtkinter.CTkFrame(self.root, width=126, height=880)
        self.frameMasuk.place(x=791, y=10)

        self.frameRun = customtkinter.CTkFrame(self.root, width=126, height=880)
        self.frameRun.place(x=927, y=10)

        self.frameCancel = customtkinter.CTkFrame(self.root, width=126, height=880)
        self.frameCancel.place(x=1063, y=10)

        self.frameNota = customtkinter.CTkFrame(self.root, width=560, height=100)
        self.frameNota.place(x=220, y=10)

        self.textBox = customtkinter.CTkTextbox(self.frameNota, width=455, height=80, fg_color='#2a2d2e', text_font=("Helvetica",25))
        self.textBox.place(x=10, y=10)

        self.buttonClose = customtkinter.CTkButton(self.frameNota, width=75, height=42, text="CLOSE", command=lambda:[self.buttonClose.place_forget(),
                                                                                                                      self.buttonOpen.place(x=475, y=29),
                                                                                                                      self.textBox.config(height=80),
                                                                                                                      self.frameNota.config(height=100)])

        self.buttonOpen = customtkinter.CTkButton(self.frameNota, width=75, height=42, text="OPEN", command=lambda:[self.buttonClose.place(x=475, y=29),
                                                                                                                    self.buttonOpen.place_forget(),
                                                                                                                    self.textBox.config(height=860),
                                                                                                                    self.frameNota.config(height=880)])
        self.buttonOpen.place(x=475, y=29)

        self.root.mainloop()


runit = Pos()



'''



    def bomba(self) :
        pass

    def kepalaLori(self) :
        pass

    def classic(self) :
        pass

    def tututKecik(self) :
        pass

    def tututBesaq(self) :
        pass

    def aima(self) :
        pass

    def atvKecik(self) :
        pass

    def atvBesaq(self) :
        pass

    def jetski(self) :
        pass

    def beam(self) :
        pass

    def princess(self) :
        pass




        self.button1 = customtkinter.CTkButton(self.frame4, width=120, height=30, text="OK")
        self.button1.pack(padx=7, pady=7)
        self.button2 = customtkinter.CTkButton(self.frame4, width=120, height=30, text="OK")
        self.button2.pack(padx=7, pady=7)
        self.button3 = customtkinter.CTkButton(self.frame4, width=120, height=30, text="OK")
        self.button3.pack(padx=7, pady=7)

        self.button4 = customtkinter.CTkButton(self.frame4, width=120, height=30, text="OK")
        self.button4.pack(padx=7, pady=7)
        self.button5 = customtkinter.CTkButton(self.frame4, width=120, height=30, text="OK")
        self.button5.pack(padx=7, pady=7)
        self.button6 = customtkinter.CTkButton(self.frame4, width=120, height=30, text="OK")
        self.button6.pack(padx=7, pady=7)


        self.frameKL = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameKL.place(x=10, y=530)

        self.frameBB = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameBB.place(x=10, y=530)

        self.frameCC = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameCC.place(x=10, y=530)

        self.frameTK = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameTK.place(x=10, y=530)

        self.frameTB = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameTB.place(x=10, y=530)

        self.frameJS = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameJS.place(x=10, y=530)

        self.frameAK = customtkinter.CTkFrame(root, width=350, height=200)
        self.frameAK.place(x=10, y=530)
        '''