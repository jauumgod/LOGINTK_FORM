

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time



class tela2:
    def __init__(self):
        self.tela2 = Tk()
        self.tela2.geometry("800x600")
        self.tela2.config(bg="BLACK")
        label1 = Label(self.tela2, text="test")
        label1.place(x=200, y=200)
        self.tela2.mainloop()
class App:
    def __init__(self):
        self.app = Tk()
        self.app.geometry("800x600")
        self.app.config(bg="BLACK")

        labelhack = Label(self.app, text="LOGIN", bg="BLACK", fg="GREEN", font="bold 19 ")
        labelhack.place(x=350, y=100)

        labelborder = Label(self.app, text="Usuario", bg="Black", fg="GREEN", font="bold 15 ")
        labelborder.place(x=350, y=200)

        userentry = Entry(self.app, width=25)
        userentry.place(x=310, y=230)

        passlabel = Label(self.app, text="Password", bg="Black", fg="GREEN", font="bold 15 ")
        passlabel.place(x=340, y=260)

        passentry = Entry(self.app, width=25, show="*")
        passentry.place(x=310, y=290)
        
        def destroy():
            user = userentry.get()
            passwd = passentry.get()
            
            if user == "joao" or passwd == "1503":
                messagebox.showinfo(message="LOGIN feito com sucesso!")
                time.sleep(2)
                self.app.destroy()
                tela2()

            else:
                messagebox.showerror(message="Usuario ou senha incorreta!")

            

        btnlogin = ttk.Button(self.app, text="LOGIN", command= destroy)
        btnlogin.place(x=350, y=320)






        self.app.mainloop()

App()
