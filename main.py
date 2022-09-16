'''
import tkinter
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

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

textbox1 = tkinter.Text(frame1, height=1, width=3, bg='gray19', font=('Helvetica',25))
textbox1.place(x=10, y=25)

############################################################

mainan = ['BB112',      # 0
          'CC191',      # 1
          'CC195',      # 2
          'TT131',      # 3
          'TT95',       # 4
          'BB103',      # 5
          'CC161',      # 6
          'TT104']      # 7

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
            print('empty space')




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
            print('empty space')

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

import customtkinter
import time

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class Pos :
    mainan = ['bomba','skuter','kepalaLori','classic','tututKecik','tututBesaq','aima','atvKecik','atvBesaq','jetski','beam','princess']
    senaraiJenis = ['BB','S','KL','CC','TK','TB','A','AK','AB','JS','B','PC']

    senarai = (
        ############################################################
        {#'bomba' : 
            'nama'      : 'Bomba',
            'jenis'     : 'BB',
            'harga'     : 15,
            'nombor'    : ['199', '192', '193', '66', '112']
        },
        ############################################################
        {#'skuter' : {
            'nama'      : 'Skuter',
            'jenis'     : 'S',
            'harga'     : 15,
            'nombor'    : ['118', '128', '46', '149', '151']
        },
        ############################################################
        {#'kepalaLori' : {
            'nama'      : 'Kepala Lori',
            'jenis'     : 'KL',
            'harga'     : 15,
            'nombor'    : ['181', '197', '152']
        },
        ############################################################
        {#'classic' : {
            'nama'      : 'Classic Car',
            'jenis'     : 'CC',
            'harga'     : 20,
            'nombor'    : ['161', '190', '191', '195', '132', '125', '113']
        },
        ############################################################
        {#'tututKecik' : {
            'nama'      : 'Tutut Kecil',
            'jenis'     : 'TK',
            'harga'     : 25,
            'nombor'    : ['92', '93', '94', '95', '131', '0', '6', '136']
        },
        ############################################################
        {#'tututBesaq' : {
            'nama'      : 'Tutut Besar',
            'jenis'     : 'TB',
            'harga'     : 30,
            'nombor'    : ['189', '200']
        },
        ############################################################
        {#'aima' : {
            'nama'      : 'Aima',
            'jenis'     : 'A',
            'harga'     : 20,
            'nombor'    : ['119', '130', '139', '176', '182']
        },
        ############################################################
        {#'atvKecik' : {
            'nama'      : 'ATV Kecil',
            'jenis'     : 'AK',
            'harga'     : 20,
            'nombor'    : ['154', '180', '185', '202', '204', '120']
        },
        ############################################################
        {#'atvBesaq' : {
            'nama'      : 'ATV Besar',
            'jenis'     : 'AB',
            'harga'     : 25,
            'nombor'    : ['211', '212']
        },
        ############################################################
        {#'jetski' : {
            'nama'      : 'JetSki',
            'jenis'     : 'JS',
            'harga'     : 20,
            'nombor'    : ['17', '146', '156', '166', '167']
        },
        ############################################################
        {#'beam' : {
            'nama'      : 'Beam',
            'jenis'     : 'B',
            'harga'     : 20,
            'nombor'    : ['4', '9', '10', '16']
        },
        ############################################################
        {#'princess' : {
            'nama'      : 'Princess Car',
            'jenis'     : 'PC',
            'harga'     : 25,
            'nombor'    : ['150', '194', '196', 'BH']
        }
        ############################################################
        
    )

    senaraiMainan = dict(zip(mainan,senarai))

    runLabel = [None]
    runDrop = [None] * 5000
    masukButton = [None] * 5000
    cancelButton = [None] * 5000
    timerMainan = [None] * 5000
    masaMainan = [None] * 5000
    masaLabel = [None] * 5000
    runList = [None]
    labelVar = vars()
    masukVar = vars()
    cancelVar = vars()

    j = 0

    z = 0

    masaLampu = 0
    masaIndex = 0


    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title('POS')
        self.root.iconbitmap('C:/Users/kebaq/Documents/GitHub/POS-system/ceriatoys.ico')
        self.root.geometry('1400x900')
        self.root.minsize(1400,900)
        #self.root.maxsize(1200,900)

        self.frameEntry = customtkinter.CTkFrame(self.root, width=200, height=100)
        self.frameEntry.place(x=10, y=10)

        self.entry1 = customtkinter.CTkEntry(self.frameEntry, width=95, height=70, text_font=('Helvetica',25), justify='center')
        self.entry1.place(x=10, y=15)
        
        self.buttonEntry = customtkinter.CTkButton(self.frameEntry, width=75, height=42, text='OK')
        self.buttonEntry.place(x=115, y=29)

        self.frameMainan = customtkinter.CTkFrame(self.root, width=770, height=770)
        self.frameMainan.place(x=10, y=120)

        self.frameMasuk = customtkinter.CTkFrame(self.root, width=75, height=880)
        self.frameMasuk.place(x=791, y=10)

        self.frameDrop = customtkinter.CTkFrame(self.root, width=75, height=880)
        self.frameDrop.place(x=881, y=10)

        self.frameRun = customtkinter.CTkFrame(self.root, width=75, height=880)
        self.frameRun.place(x=971, y=10)

        self.frameCancel = customtkinter.CTkFrame(self.root, width=75, height=880)
        self.frameCancel.place(x=1061, y=10)

        self.frameTimer = customtkinter.CTkFrame(self.root)
        self.frameTimer.place(x=1151, y=10)

        self.frameBayar = customtkinter.CTkFrame(self.root, width=75, height=880)
        self.frameBayar.place(x=1241, y=10)

        self.frameNota = customtkinter.CTkFrame(self.root, width=560, height=100)
        self.frameNota.place(x=220, y=10)

        self.textBox = customtkinter.CTkTextbox(self.frameNota, width=455, height=80, fg_color='#2a2d2e', text_font=('Helvetica',25))
        self.textBox.place(x=10, y=10)

        self.buttonClose = customtkinter.CTkButton(self.frameNota, width=75, height=42, text='Tutup', command=lambda:[self.buttonClose.place_forget(),
                                                                                                                      self.buttonOpen.place(x=475, y=29),
                                                                                                                      self.textBox.config(height=80),
                                                                                                                      self.frameNota.config(height=100)])

        self.buttonOpen = customtkinter.CTkButton(self.frameNota, width=75, height=42, text='Buka', command=lambda:[self.buttonClose.place(x=475, y=29),
                                                                                                                    self.buttonOpen.place_forget(),
                                                                                                                    self.textBox.config(height=860),
                                                                                                                    self.frameNota.config(height=880)])
        self.buttonOpen.place(x=475, y=29)

        self.loopMainan()

        self.masaWindow()

        self.root.mainloop()

    def masaWindow(self) :
        newWindow = customtkinter.CTkToplevel(self.root)
        newWindow.title("Masa mainan lampu")
        newWindow.geometry("200x200")
        newWindow.wm_transient(self.root)
        newWindow.grab_set()

        customtkinter.CTkLabel(newWindow, text='Pilih masa :', text_font=('Helvetica')).pack(pady=10)

        radio_var = customtkinter.StringVar(value=0)
        newRadio1 = customtkinter.CTkRadioButton(newWindow, text=15, variable=radio_var, value=0).pack(pady=10)
        newRadio2 = customtkinter.CTkRadioButton(newWindow, text=10, variable=radio_var, value=1).pack(pady=10)

        customtkinter.CTkButton(newWindow, width=75, height=42,
                                command=lambda: [self.setMasa(radio_var.get()), newWindow.destroy()],
                                text='OK', 
                                text_font=('Helvetica',11)).pack(pady=10)

    
    def setMasa(self,x) :
        self.masaLampu = int(x)


    def loopMainan(self) :
        for key, val in self.senaraiMainan.items() :
            customtkinter.CTkLabel(self.frameMainan, width=75, height=42, text=self.senaraiMainan[key]['nama'], text_font=('Helvetica',11)).grid(row=self.j, column=0)

            for i in range(len(self.senaraiMainan[key]['nombor'])) :
                self.listMainan(self.senaraiMainan[key]['jenis'],self.senaraiMainan[key]['harga'],self.senaraiMainan[key]['nombor'][i],i)
            
            self.j+=1


    def listMainan(self,jenis,harga,nombor,index) :
        customtkinter.CTkButton(self.frameMainan, width=75, height=42,
                                command=lambda: self.running(jenis,harga,nombor),
                                text=jenis+' '+nombor, 
                                text_font=('Helvetica',11)).grid(row=self.j, column=index+1, padx=4, pady=11)


    def running(self,jenis,harga,nombor) :
        for runIndex in range(len(self.runLabel)) :
            runIndex = len(self.runLabel)

            break
        
        self.runLabel.append(customtkinter.CTkEntry(self.frameRun, width=75, height=42, text_font=('Helvetica',10)))
        self.runLabel[runIndex].insert(0,nombor)
        self.runLabel[runIndex].pack(pady=1)

        clicked = customtkinter.StringVar()
        clicked.set(jenis)
        self.runDrop[runIndex] = customtkinter.CTkOptionMenu(self.frameDrop, values=self.senaraiJenis, variable=clicked, width=75, height=42, text_font=('Helvetica',15))
        self.runDrop[runIndex].pack(pady=1)

        self.masukButton[runIndex] = customtkinter.CTkButton(self.frameMasuk, width=75, height=42, text='Masuk', text_font=('Helvetica',10), command=lambda: self.masuk(runIndex,jenis,nombor))
        self.masukButton[runIndex].pack(pady=1)

        self.cancelButton[runIndex] = customtkinter.CTkButton(self.frameCancel, width=75, height=42, text='Cancel', text_font=('Helvetica',10), command=lambda: self.cancel(runIndex))
        self.cancelButton[runIndex].pack(pady=1)

        if jenis in ('BB','S','KL') :
            self.masaMainan[runIndex] = 900
        else :
            if self.masaLampu == 0 :
                self.masaMainan[runIndex] = 900
            else :
                self.masaMainan[runIndex] = 600

        self.timerMainan[runIndex] = customtkinter.CTkFrame(self.frameTimer, width=75, height=42)
        self.timerMainan[runIndex].pack(pady=1)

        self.timerLabel(runIndex)

        


    def masuk(self,runIndex,jenis,nombor) :
        self.runLabel[runIndex].destroy()
        self.runDrop[runIndex].destroy()
        self.masukButton[runIndex].destroy()
        self.cancelButton[runIndex].destroy()

        try :
            with open('docs/readme.txt', 'a') as f :
                f.write(jenis+' '+nombor+'\n')
        except FileNotFoundError:
            with open('C:/Users/kebaq/Desktop/sale.txt', 'w') as f :
                f.write(jenis+' '+nombor+'\n')

        
        f.write('\n'+jenis+' '+nombor)
        


    def cancel(self,runIndex) :
        self.runLabel[runIndex].destroy()
        self.runDrop[runIndex].destroy()
        self.masukButton[runIndex].destroy()
        self.cancelButton[runIndex].destroy()


    def timerLabel(self,runIndex) :
        self.masaLabel[self.masaIndex] = customtkinter.CTkLabel( self.timerMainan[runIndex], text='0', width=75, height=42)
        self.masaLabel[self.masaIndex].pack()
        self.masaLabel[self.masaIndex].after(1000, self.update(self.masaLabel[self.masaIndex],self.masaMainan[runIndex]))
        self.masaIndex+=1


    def update(self,index,masa) :
        x = 0
        while (x <= masa) :
            x+=1
            index.configure(text=str(x))
        
        #newMasa = int(masa)-1
        #index.configure(text=str(newMasa))
        #index.after(1000, self.update(index,newMasa))

#        masaLabel = [None] * 5000
#        masaLabel[index] = customtkinter.CTkLabel(parent, text=masa, width=75, height=42)
#        masaLabel[index].pack()
        


if __name__ == '__main__':
    Pos()


'''

self.mainanButton[z] = customtkinter.CTkButton(self.frameMainan, width=75, height=42,
                                        command=lambda: customtkinter.CTkLabel(self.frameRun, width=75, height=42, text=self.senaraiMainan[key]['jenis']+' '+self.senaraiMainan[key]['nombor'][i]).pack(),
                                        text=self.senaraiMainan[key]['jenis']+' '+self.senaraiMainan[key]['nombor'][i])

self.mainanButton[z].grid(row=j, column=i+1, padx=4, pady=11)##################self.mainanButton list repair the list looping
                




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




        self.button1 = customtkinter.CTkButton(self.frame4, width=120, height=30, text='OK')
        self.button1.pack(padx=7, pady=7)
        self.button2 = customtkinter.CTkButton(self.frame4, width=120, height=30, text='OK')
        self.button2.pack(padx=7, pady=7)
        self.button3 = customtkinter.CTkButton(self.frame4, width=120, height=30, text='OK')
        self.button3.pack(padx=7, pady=7)

        self.button4 = customtkinter.CTkButton(self.frame4, width=120, height=30, text='OK')
        self.button4.pack(padx=7, pady=7)
        self.button5 = customtkinter.CTkButton(self.frame4, width=120, height=30, text='OK')
        self.button5.pack(padx=7, pady=7)
        self.button6 = customtkinter.CTkButton(self.frame4, width=120, height=30, text='OK')
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