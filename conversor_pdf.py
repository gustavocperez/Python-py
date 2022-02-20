import tkinter as tk
from tkinter import ttk
from tkinter.constants import PAGES
from tkinter.filedialog import askopenfilename
import tabula
from tabula.io import read_pdf
from openpyxl import load_workbook
import os


class Principal:
    def __init__(self, win):
        self.lbNome=tk.Label(win, text="Escolha o arquivo em pdf")
        self.btnEscolher=tk.Button(win, text="Procurar", command=self.fprocurar)
        self.lbNomeArquivo=tk.Label(win)
        self.lbNome.place(x=180, y=50)
        self.btnEscolher.place(x=225, y=100)
        self.lbNomeArquivo.place(x=100, y=150)

    def fprocurar(self):
        #adicionar verificar de arquivo pdf
        filename = askopenfilename()
        self.lbNomeArquivo.config(text=filename)
        df = tabula.read_pdf(filename, pages="all")
        name = filename.split("/")
        for i in name:
            name1 = i
        name2 = name1.strip('.pdf')
        for i in df:
            i.to_excel(f'{name2}.xlsx')
        os.startfile(f'{name2}.xlsx')


janela = tk.Tk()
principal = Principal(janela)
janela.title("Bem Vindo ao Conversor de PDF para Excel")
janela.geometry("500x400+10+10")
janela.mainloop()