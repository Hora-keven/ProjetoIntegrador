import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import openpyxl


class Bot:
    def __init__(self):
        self.navegador = webdriver.Chrome()
        self.navegador.maximize_window()
        self.abrir_site()
        self.varrer_site()
        self.excel()

    def abrir_site(self):
        self.navegador.get("file:///C:/Users/53688621808/Documents/PI/site/carrinho.html")

    def varrer_site(self):
        self.lista_valor = []
        self.nome = []
        sleep(5)
        for i in range(16):
            self.lista_valor.append(self.navegador.find_element(By.XPATH, f"/html/body/main/div/div[{i+1}]/div[1]").text)
            self.nome.append(self.navegador.find_element(By.XPATH, f"/html/body/main/div/div[{i+1}]/div[2]").text)



    def excel(self):
        planilha = {'nome': self.nome, 'valor': self.lista_valor}
        data = pd.DataFrame(planilha)
        data.to_excel('planilha_valor.xlsx')
        data.to_csv('planilha_valor.csv')





t = Bot()
