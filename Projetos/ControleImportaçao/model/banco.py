import mysql.connector

class Banco:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'controleimportacao',
            password='Controle@2026',
            database = 'controleimportacao'
        )

        self.meucursor = self.db.cursor()
    def Criar_tabela(self):
        self.meucursor.execute(" CREATE TABLE fornecedores (CODIGO int (6), NOME varchar (20), MOEDA varchar (15), INCOTERM varchar (4), FORM_PAG varchar (20), PAIS_ORIGEM varchar (15), ENDERECO varchar (50),FRETE varchar (10), PROCEDENCIA varchar (50))")

