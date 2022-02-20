import sqlite3
from tkinter import *
from datetime import date
from sqlite3 import Error

def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def insert_data():
    database = "C:/Users/TEMP/Dropbox/Python/custo_op.db"

    conn = create_connection(database)

    sql = ''' INSERT INTO custoop(ano, mes, valor) 
                VALUES(?,?,?)'''
    
    project = (2021, "Setembro", 0.45)
    
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    conn.close()

def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM custoop")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = "C:/Users/TEMP/Dropbox/Python/custo_op.db"

    conn = create_connection(database)

    with conn:
        select_all(conn)

if __name__ == '__main__':
    main()

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
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        

        self.titulo = Label(self.container1, text="Digite a data de entrada e de saida:")
        self.titulo["font"] = ("Calibri", "14", "bold")
        self.titulo.pack()

        self.entrada = Label(self.container2, text="Data inicial")
        self.entrada["font"] = ("Calibri", "14", "bold")
        self.entrada.pack(side=LEFT)

        self.datae = Entry(self.container2)
        self.datae["width"] = 15
        self.datae["font"] = self.fonte
        self.datae.pack(side=RIGHT)

        self.saida = Label(self.container3, text="Data Final")
        self.saida["font"] = ("Calibri", "14", "bold")
        self.saida.pack(side=LEFT)

        self.saidae = Entry(self.container3)
        self.saidae["width"] = 15
        self.saidae["font"] = self.fonte
        self.saidae.pack(side=RIGHT)

        self.btn = Button(self.container4, text="Converter", font=self.fonte, width=10)
        self.btn["command"] = self.calcularop
        self.btn["padx"] = 10
        self.btn["width"] = 20
        self.btn.pack(side=RIGHT)

        self.lblmsg = Label(self.container5, text="")
        self.lblmsg["font"] = ("Verdana", "12", "italic")
        self.lblmsg.pack()


    def calcularop(self):

        meses = [(1,31,1,0.45),(1,28,2,0.43),(1,31,3,0.43),(1,30,4,0.43),(1,31,5,0.413),(1,30,6,0.4087),(1,31,7,0.3728),(1,31,8,0.3645)]

        j = 0

        op = 0
        opplus = 0
        custoop = 0
        dias = 0

        data_ini = self.datae.get()
        data_fim = self.saidae.get()

        datai = data_ini.split('/')
        diaini = int(datai[0])
        mesini = int(datai[1])
        anoini = int(datai[2])

        dataf = data_fim.split('/')
        diafim = int(dataf[0])
        mesfim = int(dataf[1])
        anoini = int(dataf[2])

        for i in meses:

            if mesini > meses[j][2] or mesfim < meses[j][2]:
                op = 0
            elif mesini == meses[j][2]:
                op = meses[j][1] - diaini + 1
                dias = dias + op
                custoop = op * meses[j][3]
                opplus = opplus + custoop
            elif mesini < meses[j][2] and mesfim > meses[j][2]:
                op = meses[j][1] - meses[j][0] + 1 
                dias = dias + op
                custoop = op * meses[j][3]
                opplus = opplus + custoop
            else:
                op = diafim - meses[j][0] + 1
                dias = dias + op
                custoop = op * meses[j][3]
                opplus = opplus + custoop
            
            j = j + 1

        print("Dias: ", dias, "\n", "Custo op total:", opplus, "Custo op médio:", f'{(opplus/dias):.3f}')
        

        self.lblmsg["text"] = ("Dias: ", dias, "\n", "Custo op medio:", f'{(opplus/dias):.3f}')

        

root = Tk()
Application(root)
root.mainloop()