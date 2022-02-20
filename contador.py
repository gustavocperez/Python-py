import tkinter as tk

counter = "Gustavo"
def counter_label(label):
  def count():
    global counter
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Nome e Sobrenome")

label = tk.Label(root, fg="green", text="AQUI!")
label.grid(row=4)

counter_label(label)

tk.Label(root, text="Nome:").grid(row=0, column=0)
tk.Label(root, text="Nome:").grid(row=0, column=0)

button1 = tk.Button(root, text='Mostar', width=25).grid(row=1)

button2 = tk.Button(root, text='Stop', width=25, command=root.destroy).grid(row=2)

root.mainloop()