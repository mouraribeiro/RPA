from tkinter import *

janela = Tk()


janela.title("Interface")

janela.geometry("600x600")

instrucao = Label(text="\nOlá, Mundo!", font='Arial 30')
rotulo = Label(text="Python", font="arial 32",relief="flat",background="darkgrey",foreground="red")

rotulo2 = Label(text="Python", font="arial 32",relief="groove",background="darkgrey",foreground="black")

rotulo3 = Label(text="Python", font="arial 32",relief="ridge",background="darkgrey",foreground="blue")

rotulo4 = Label(text="Python", font="arial 32",relief="raised",background="darkgrey",foreground="blue")

rotulo5 = Label(text="Python", font="arial 32",relief="solid",background="darkgrey",foreground="blue")

rotulo6 = Label(text="Python", font="arial 32",relief="sunken",background="darkgrey",foreground="blue")
rotulo.pack()
rotulo2.pack()
rotulo3.pack()
rotulo4.pack()
rotulo5.pack()
rotulo6.pack()
instrucao.pack()


janela.mainloop()