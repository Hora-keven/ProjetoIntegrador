from tkinter import *
from tkinter import ttk
import banco
from bot import Bot
import awesometkinter as atk
import os
import pandas as pd
import openpyxl
pastaApp = os.path.dirname(__file__)

telinha = Tk()


class Tela:
    def __init__(self):
        self.telinha = telinha
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.lista_frame2()
        self.opcao()
        self.insere()
        telinha.mainloop()

    def tela(self) -> None:
        """
        Função que cria a tela
        :return: None
        """
        self.telinha.title("Celulares")
        self.telinha.configure(background="#FFFFFF")
        self.telinha.maxsize(width=1920, height=1080)
        self.telinha.minsize(width=1920, height=1080)
        self.telinha.resizable(True, True)
        self.zoom()

    def frames(self) -> None:
        """
        Função que cria os frames da Tela
        :return: None
        """
        self.frame = atk.Frame3d(self.telinha, bg="#612a92")
        self.frame.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_2 = atk.Frame3d(self.telinha, bg='#612a92')
        self.frame_2.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.25)

        self.frame_3 = atk.Frame3d(self.telinha, bg='#612a92')
        self.frame_3.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self) -> None:
        """
        Função que criar os botões da tela
        :return: None
        """
        self.botao_confirma = Button(self.frame_2, text="Confirmar", bg='#8ae287', command=self.procura)
        self.botao_confirma.place(relx=0.40, rely=0.41, relwidth=0.12, relheight=0.15)

    def labels(self) -> None:
        """
        Função que cria os labels, ou seja os textos que aparecem na tela
        :return: None
        """
        self.lb_input = Label(self.frame_2, font=("Arial", 15), text='Escreva qual a marca:  ', bg='#612a92')
        self.lb_input.place(relx=0.005, rely=0.40, relwidth=0.20, relheight=0.15)

        self.lbtitulo = Label(self.frame, image=self.img_zoom)
        self.lbtitulo.place(relx=0.05, rely=0.25, relheight=0.37, relwidth=0.07)

        self.lbStatus = Label(self.frame_2, font=("Arial", 25), text='', fg='black', bg='#612a92')
        self.lbStatus.place(relx=0.15, rely=0.70, relwidth=0.70, relheight=0.15)



    def lista_frame2(self) -> None:
        """
        Função que cria lista que aoarece na tela
        :return: None
        """
        self.listaCli = ttk.Treeview(self.frame_3, height=3, columns=('col1', 'col2', 'col3'))

        self.listaCli.heading('#1', text='Marca')
        self.listaCli.heading('#2', text='Modelo')
        self.listaCli.heading('#3', text='Valor')

        self.listaCli.column('#1', width=100)
        self.listaCli.column('#2', width=100)
        self.listaCli.column('#3', width=100)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.94, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_3, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)

    def insere(self) -> None:
        """
        Função que pega do banco de dados as informações e mostra na tela
        :return: None
        """
        self.listaCli.delete(*self.listaCli.get_children())
        for i in banco.cursor.execute(f"SELECT * FROM celulares"):
            self.listaCli.insert(parent="", index=0, values=i)

    def procura(self) -> None:
        """
        Função que procura no banco de dados de acordo com o que o usuario quer.
        :return: None
        """
        self.listaCli.delete(*self.listaCli.get_children())

        Bot(marca=self.clicked.get().lower())


    def zoom(self):
        self.img_zoom = PhotoImage(file=pastaApp+"//zoom.logo.png")

    def opcao(self):
        options = [
            "Celulares",
            "Samsung",
            "Motorola",
            "Xiaomi",
            "Multilaser",
            "Iphone"
        ]
        self.clicked = StringVar()
        self.clicked.set("Celulares")
        drop = OptionMenu(self.frame_2, self.clicked, *options)
        drop.place(relx=0.18, rely=0.41, relwidth=0.20, relheight=0.15)




