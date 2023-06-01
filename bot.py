from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import openpyxl
import banco

class Bot:
    def __init__(self, marca):
        self.marca = marca
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.navegador = webdriver.Chrome(options=options)
        self.navegador.maximize_window()
        self.bot()
        self.remove_banco_dados()
        self.add_banco_dados()

    def bot(self) -> None:
        self.navegador.get("https://www.zoom.com.br/celular/$opcao$".replace("$opcao$", f"{self.marca}"))
        """
        Função que pega os celulares das marcas
        :return: None
        """


        self.lista_nome = []
        self.lista_marca = []
        self.lista_valor = []

        i = 0
        while True:
            i += 1
            if i == 6:
                i += 4
            if self.marca == "celulares":
                if len(self.lista_marca) == 15:
                    break
            else:
                if len(self.lista_marca) == 10:
                    break
            var = self.navegador.find_element(By.XPATH,
                                              f"/html/body/div[1]/div[1]/div/div[2]/div[3]/div[{i + 1}]/a/div[2]/div[2]/div[1]/div[1]/h2").text.split()
            self.tira_espaco_nome = "".join(var[0:5])
            if not self.tira_espaco_nome in self.lista_nome:
                try:
                    self.lista_marca.append(var[1])

                    var_valor = self.navegador.find_element(By.XPATH, f"/html/body/div/div/div/div[2]/div[3]/div[{i+1}]/a/div[2]/div[2]/div[2]/p[1]").text.split()

                    self.tira_espaco_valor = "".join(var_valor[0:4])
                    self.lista_valor.append(self.tira_espaco_valor)
                    self.lista_nome.append(self.tira_espaco_nome)
                except:
                    pass
            else:
                continue
        self.opcao_csv()


    def add_banco_dados(self) -> None:
        """
        Função que adiciona no banco de dados todos os celulares
        :return: None
        """

        for i in range(len(self.lista_marca)):
            banco.cursor.execute(f"INSERT INTO celulares VALUES ('{self.marca}','{self.tira_espaco_nome}','{self.tira_espaco_valor}')")

            banco.banco.commit()

    def remove_banco_dados(self) -> None:
        """
        Função que remove os dados antigos do banco
        :return: None
        """
        banco.cursor.execute("DELETE FROM celulares ")
        banco.banco.commit()

    def opcao_csv(self):

        cabecalho = {f'Marca': self.lista_marca,
                     'modelo': self.tira_espaco_nome,
                     'valor': self.tira_espaco_valor}

        data = pd.DataFrame(cabecalho)
        data.to_csv(f'{self.marca}.csv', sep=";", index=False)

        data.to_excel(f'{self.marca}.xlsx', index=False)






