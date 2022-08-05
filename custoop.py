import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error



def create_connection2(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def show():
    database = "custo_op.db"
    conn = create_connection2(database)
    cur = conn.cursor()
    cur.execute("select * from custoop")

    listBox.delete(*listBox.get_children())

    tempList = cur.fetchall()
    # tempList.sort(key=lambda e: e[1], reverse=True)

    print(tempList)

    for i, (id, ano, mes, valor, mes_num, dia_ini, dia_fim) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(id, ano, mes, valor))


def calcularop():

    meses = [(1, 31, 1), (1, 28, 2), (1, 31, 3), (1, 30, 4), (1, 31, 5), (1, 30, 6), (1, 31, 7), (1, 31, 8),
             (1, 30, 9), (1, 31, 10), (1, 30, 11), (1, 31, 12)]

    j = 0

    op = 0
    opplus = 0
    custoop = 0
    dias = 0

    data_ini = input_dataini.get()
    data_fim = input_datafin.get()

    if data_ini == '' or data_fim == '':
        messagebox.showinfo("Alerta", "Prencha os campos!")

    else:
        try:
            datai = data_ini.split('/')
            diaini = int(datai[0])
            mesini = int(datai[1])
            anoini = int(datai[2])
        except:
            return messagebox.showinfo('Alerta', 'Digite o ano da data inicial!')

        try:
            dataf = data_fim.split('/')
            diafim = int(dataf[0])
            mesfim = int(dataf[1])
            anofim = int(dataf[2])
        except:
            return messagebox.showinfo('Alerta', 'Digite o ano da data final!')

        if mesfim < mesini and anofim <= anoini:
            messagebox.showinfo('Alerta', "A Data Final não pode ser menor ou igual a Data Inicial!")

        else:
            database = "custo_op.db"
            conn = create_connection2(database)
            cur = conn.cursor()

            datai = data_ini.split('/')
            diaini = int(datai[0])
            mesini = int(datai[1])
            anoini = int(datai[2])

            if anoini > 2021:
                dif_ano = anoini - 2021
                mesini = mesini + (12 * dif_ano)


            dataf = data_fim.split('/')
            diafim = int(dataf[0])
            mesfim = int(dataf[1])
            anofim = int(dataf[2])

            if anofim > 2021:
                dif_ano2 = anofim - 2021
                mesfim = mesfim + (12 * dif_ano2)

            sql_buscar = ("select * from custoop")

            cur.execute(sql_buscar)

            tempList = cur.fetchall()

            for i in tempList:

                if mesini > tempList[j][4] or mesfim < tempList[j][4]:
                    op = 0
                elif mesini == tempList[j][4]:
                    op = tempList[j][6] - diaini + 1
                    dias = dias + op
                    custoop = op * tempList[j][3]
                    opplus = opplus + custoop
                elif mesini < tempList[j][4] and mesfim > tempList[j][4]:
                    op = tempList[j][6] - tempList[j][5] + 1
                    dias = dias + op
                    custoop = op * tempList[j][3]
                    opplus = opplus + custoop
                else:
                    op = diafim - tempList[j][5] + 1
                    dias = dias + op
                    custoop = op * tempList[j][3]
                    opplus = opplus + custoop

                j = j + 1

            j = 0

            value = ("Dias: ", dias, "\n", "Custo op medio:", f'{(opplus / dias):.3f}')

            my_string_var.set(value)


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def cadastrar():
    meses = [(1, "Janeiro", 31), (2, "Fevereiro", 28), (3, "Março", 31), (4, "Abril", 30), (5, "Maio", 31),
             (6, "Junho", 30), (7, "Julho", 31), (8, "Agosto", 31), (9, "Setembro", 30), (10, "Outubro", 31),
             (11, "Novembro", 30), (12, "Dezembro", 31)]

    database = "custo_op.db"

    conn = create_connection(database)

    ano = input_ano.get()
    mes = input_mes.get()
    valor = input_custo.get()
    valor = valor.replace(',', '.')
    mes_nome = ''

    print(ano)
    print('\n', mes)
    print('\n', valor)

    listBox.selection_clear()

    if ano == '' or mes == '' or valor == '':

        messagebox.showinfo("Alerta", "Preencha todos os campos!")

    else:

        if len(mes) > 2:
            messagebox.showinfo("Alerta", "O mês deve ser preenchido no formato de número")

        else:

            mes = int(mes)

            j = 0

            for i in meses:

                if mes == meses[j][0]:
                    mes_nome = meses[j][1]
                    dia_fim = meses[j][2]

                j = j + 1

            sql = ''' INSERT INTO custoop(ano, mes, valor, mes_num, dia_ini, dia_fim) 
                        VALUES(?,?,?,?,?,?)'''

            if int(ano) > 2021:
                dif_ano = int(ano) - 2021
                mes = mes + (12 * dif_ano)

            project = (ano, mes_nome, valor, mes, 1, dia_fim)

            cur = conn.cursor()
            cur.execute(sql, project)
            conn.commit()
            show()
            conn.close()
            messagebox.showinfo("Alerta", "Informações cadastradas com sucesso!")


def handle_click(event):
    meses = [(1, "Janeiro"), (2, "Fevereiro"), (3, "Março"), (4, "Abril"), (5, "Maio"), (6, "Junho"), (7, "Julho"),
             (8, "Agosto"), (9, "Setembro"), (10, "Outubro"), (11, "Novembro"), (12, "Dezembro")]
    mes_nome = ''
    j = 0

    selected = listBox.focus()
    text = listBox.item(selected, 'values')

    if text != '':

        for i in meses:

            if text[2] == meses[j][1]:
                mes_nome = meses[j][0]

            j = j + 1

        input_ano.delete(0, END)
        input_ano.insert(0, text[1])
        input_mes.delete(0, END)
        input_mes.insert(0, mes_nome)
        input_custo.delete(0, END)
        input_custo.insert(0, text[3])
        input_id.delete(0, END)
        input_id.insert(0, text[0])
    else:
        ''

def handle_click2(event):
    meses = [(1, "Janeiro"), (2, "Fevereiro"), (3, "Março"), (4, "Abril"), (5, "Maio"), (6, "Junho"), (7, "Julho"),
             (8, "Agosto"), (9, "Setembro"), (10, "Outubro"), (11, "Novembro"), (12, "Dezembro")]
    mes_nome = ''
    j = 0

    selected = listBox.focus()
    text = listBox.item(selected, 'values')

    if text != '':

        for i in meses:

            if text[2] == meses[j][1]:
                mes_nome = meses[j][0]

            j = j + 1

        input_id.delete(0, END)
        input_id.insert(0, text[0])
    else:
        ''

def editar():
    meses = [(1, "Janeiro"), (2, "Fevereiro"), (3, "Março"), (4, "Abril"), (5, "Maio"), (6, "Junho"), (7, "Julho"),
             (8, "Agosto"), (9, "Setembro"), (10, "Outubro"), (11, "Novembro"), (12, "Dezembro")]
    mes_nome = ''

    database = "custo_op.db"

    conn = create_connection(database)

    sql_update_ano = '''UPDATE custoop SET ano = ? WHERE id = ?'''
    sql_update_mes = '''UPDATE custoop SET mes = ? WHERE id = ?'''
    sql_update_mes_num = '''UPDATE custoop SET mes_num = ? WHERE id = ?'''
    sql_update_valor = '''UPDATE custoop SET valor = ? WHERE id = ?'''

    id = input_id.get()

    if id != "":

        mes = int(input_mes.get())

        if len(str(mes)) > 2:
            messagebox.showinfo("Alerta", "O mês deve ser preenchido no formato de número")

        else:

            j = 0

            for i in meses:

                if mes == meses[j][0]:
                    mes_nome = meses[j][1]

                j = j + 1

            valor = input_custo.get()
            valor1 = valor.replace(',', '.')

            mes_final = (mes_nome, id)
            valor1 = (input_custo.get(), id)
            ano = (input_ano.get(), id)
            mes = (mes, id)

            conn.execute(sql_update_ano, ano)
            conn.execute(sql_update_mes, mes_final)
            conn.execute(sql_update_mes_num, mes)
            conn.execute(sql_update_valor, valor1)
            conn.commit()
            show()
            conn.close()

            input_ano.delete(0, END)
            input_mes.delete(0, END)
            input_id.delete(0, END)
            input_custo.delete(0, END)
            messagebox.showinfo("Alerta", "Informações EDITADAS com sucesso!")
    else:
        messagebox.showinfo("Alerta", "Preencha todos os campos!")


def excluir():
    database = "custo_op.db"

    conn = create_connection(database)

    id = input_id.get()

    if id != '':

        sql_delete = '''DELETE FROM custoop WHERE id = ?'''
        conn.execute(sql_delete, [id])
        conn.commit()
        conn.close()

        show()

        input_ano.delete(0, END)
        input_mes.delete(0, END)
        input_id.delete(0, END)
        input_custo.delete(0, END)
        messagebox.showinfo("Alerta", "Informações EXCLUÍDAS com sucesso!")

    else:
        messagebox.showinfo("Alerta", "Selecione o item a ser excluído")


custoop = tk.Tk()

my_string_var = StringVar()
my_string_var.set('')

label = tk.Label(custoop, text="Custo Operacional", font=("Arial", 30)).grid(row=0, columnspan=4)
label_dataini = tk.Label(custoop, text="Digite a data Inicial: ", font=("Arial", 15)).grid(row=1, column=0)
input_dataini = tk.Entry(custoop)
input_dataini.grid(row=1, column=1)
label_datafin = tk.Label(custoop, text="Digite a data Final: ", font=("Arial", 15)).grid(row=2, column=0)
input_datafin = tk.Entry(custoop)
input_datafin.grid(row=2, column=1)
label_custo = tk.Label(custoop, textvariable=my_string_var, font=("Arial", 15))
label_custo.grid(row=3, columnspan=4)
calcButton = tk.Button(custoop, text="Calcular", width=15, height=2, command=calcularop).grid(row=1, column=2)

cols = ('ID', 'Ano', 'Mês', 'Valor')
listBox = ttk.Treeview(custoop, columns=cols, show='headings', selectmode='browse')
vsb = ttk.Scrollbar(orient="vertical", command=listBox.yview)
vsb.place(x=785, y=165, height=211)

listBox.configure(yscrollcommand=vsb.set)

for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=4, column=0, columnspan=4)

label_ano = tk.Label(custoop, text="Digite o ano: ", font=("Arial", 15)).grid(row=5, column=0)
input_ano = tk.Entry(custoop)
input_ano.grid(row=5, column=1)

label_mes = tk.Label(custoop, text="Digite o mês em número: ", font=("Arial", 15)).grid(row=6, column=0)
input_mes = tk.Entry(custoop)
input_mes.grid(row=6, column=1)
label_mes_ex = tk.Label(custoop, text="Ex: Setembro = 9", font=("Arial", 10)).grid(row=6, column=2)
label_custo = tk.Label(custoop, text="Custo Operacional", font=("Arial", 15)).grid(row=7, column=0)
input_custo = tk.Entry(custoop)
input_custo.grid(row=7, column=1)
label_esp = tk.Label(custoop).grid(row=8, column=0)

cadastarButoon = tk.Button(custoop, text="Cadastrar", width=15, command=cadastrar).grid(row=9, column=0)
editarButton = tk.Button(custoop, text="Editar", width=15, command=editar).grid(row=9, column=1)
excluirButton = tk.Button(custoop, text="Excluir", width=15, command=excluir).grid(row=9, column=2)

label_esp2 = tk.Label(custoop).grid(row=10, column=0)
input_id = tk.Entry(custoop, width=1)

input_id.grid(row=11, column=0)

show()

custoop.bind("<Double-1>", handle_click)
custoop.bind("<Button-1>", handle_click2)

custoop.mainloop()

