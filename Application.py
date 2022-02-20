from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "14")

        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.titulo = Label(self.container1, text="Informe a Temperatura em Graus \n que deseja converter para Farenheit:")
        self.titulo["font"] = ("Calibri", "14", "bold")
        self.titulo.pack()

        self.temp = Entry(self.container2)
        self.temp["width"] = 5
        self.temp["font"] = self.fonte
        self.temp.pack(side=LEFT)

        self.btn = Button(self.container2, text="Converter para Celsius", font=self.fonte, width=10)
        self.btn["command"] = self.converterInfo1
        self.btn["padx"] = 10
        self.btn["width"] = 20
        self.btn.pack(side=RIGHT)

        self.temp1 = Entry(self.container3)
        self.temp1["width"] = 5
        self.temp1["font"] = self.fonte
        self.temp1.pack(side=LEFT)

        self.btn = Button(self.container3, text="Converter para Farenheit", font=self.fonte, width=10)
        self.btn["command"] = self.converterInfo2
        self.btn["padx"] = 10
        self.btn["width"] = 20
        self.btn.pack(side=RIGHT)

        self.lblmsg = Label(self.container4, text="")
        self.lblmsg["font"] = ("Verdana", "12", "italic")
        self.lblmsg.pack()

    def converterInfo1(self):

        num = (float(self.temp.get())-32)*5/9

        self.lblmsg["text"] = ("{0:.2f} Celsius".format(num))
    
    def converterInfo2(self):

        num = (float(self.temp1.get())*9/5)+32

        self.lblmsg["text"] = ("{0:.2f} Farenheit".format(num))
    

root = Tk()
Application(root)
root.mainloop()