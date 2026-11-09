from model.banco import Banco
from model.modelofornecedor import ModeloFornecedor

banco = Banco()

def Inserir_dados(self, forcenecedor:ModeloFornecedor)-> bool:
        dados_sql = """INSERT INTO fornecedores 
        (CODIGO, NOME, MOEDA, INCOTERM, FORM_PAG, PAIS_ORIGEM, ENDERECO, FRETE, PROCEDENCIA)
        values (%s, %s, %s, %s, %s, %s,%s, %s,%s)"""

        valor = (forcenecedor.codigo, forcenecedor.nome, forcenecedor.moeda, forcenecedor.incoterm, forcenecedor.form_pag, forcenecedor.pais_origem, forcenecedor.endereco,forcenecedor.frete, forcenecedor.procedencia)

        banco.meucursor.execute(dados_sql, valor)
        banco.db.commit()


def Leitura_all_dados(self):

        self.meucursor.execute(" SELECT * FROM fornecedores")

        resultados_dados = self.meucursor.fetchall()

        for resultados in resultados_dados:
            print(resultados)

def fechar_conexao(self):
        self.meucursor.close()
        self.db.close()

