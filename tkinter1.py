import tkinter as tk
from tkinter.ttk import *


def mostrar():
    n = nome.get()
    s = sobre.get()
    ns = n + " " + s
    print(ns)
    newWindow = tk.Toplevel(janela)
    newWindow.title("Resultado")
    newWindow.geometry("200x200")
    label = tk.Label(newWindow, text ="")
    label.grid(row=0)
    label.config(text=str(ns))

def mostrar2():
    n = nome.get()
    s = sobre.get()
    ns = n + " " + s
    print(ns)
    lb.config(text=str(ns))
    

janela = tk.Tk()
janela.title("Exemplo Tkinter")
janela.geometry("300x150")

tk.Label(janela, text="Nome:").grid(row=0)
tk.Label(janela, text="Sobrenome:").grid(row=1)
lb = tk.Label(janela, text="Label")
lb.grid(row=4)

nome = tk.Entry(janela)
sobre = tk.Entry(janela)
nome.grid(row=0, column=1)
sobre.grid(row=1, column=1)

tk.Button(janela, text="Mostrar em Nova Janela!", command=mostrar).grid(row=3, column=1)
tk.Button(janela, text="Mostrar!", command=mostrar2).grid(row=2, column=1)
tk.Button(janela, text="Sair", command=janela.quit).grid(row=2, column=0)

tk.mainloop()