from model import bancofornecedor
from model.modelofornecedor import ModeloFornecedor



def preencher():

        novodado = ModeloFornecedor(1006,"3 wells","u$","FCA","ANTECIPADO","CHINA","CHINA TWON","COLLECT","china")
        bancofornecedor.Inserir_dados(novodado)



def VisualizarFornecedores():
    ManipulacaoBanco.Leitura_all_dados()


preencher()