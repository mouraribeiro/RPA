from tkinter import *

janela = Tk()


janela.title("Interface")

janela.geometry("600x600")

nome = Label(text="Nome: ", font="Arial 18")

nome.grid(column=0, row=1,sticky="W",padx=5,pady=10)  

entrada = Entry(font="Arial 18",relief="ridge")
entrada.grid(column=1, row=1,sticky="W",padx=5,pady=10)

sobrenome = Label(text="Sobrenome: ", font="Arial 18")

sobrenome.grid(column=0, row=2,sticky="W",padx=5,pady=10)  

entrada = Entry(font="Arial 18",relief="ridge")
entrada.grid(column=1, row=2,sticky="W",padx=5,pady=10)


janela.mainloop()