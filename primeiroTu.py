from tkinter import *
from tkinter import ttk,messagebox
root = Tk()
frm = ttk.Frame(root, padding=100,width=300)
frm.grid()


def teste():
    messagebox.showinfo("TESTE,deu ruim!")
    
    

ttk.Label(frm, text="Hello World!").grid(column=0, row=1)
ttk.Button(frm, text="Teste", command=teste).grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)

root.mainloop()