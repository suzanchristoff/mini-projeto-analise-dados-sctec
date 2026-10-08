# Função para calcular a receita gerada por cada tipo de produto, canal de vendas e região
def calcular_receita(dataframe, regiao= "Todas", produto = "Todos", canal = "Todas"):
  '''Função com parâmetros default para filtrar o DataFrame por região,
    produto ou canal de vendas retornando o valor total de vendas
  '''
  if regiao != "Todas":
    dataframe = dataframe[dataframe['Região']==regiao]
  if produto != "Todos":
    dataframe = dataframe[dataframe['Produto']==produto]
  if canal != "Todas":
    dataframe = dataframe[dataframe['Canal']==canal]
  return round(dataframe["Valor_Venda"].sum(), 2)