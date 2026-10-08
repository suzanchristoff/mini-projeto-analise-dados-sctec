# Importação bibliotecas
import pandas as pd

# Atribuição dos dados à variável df
df = pd.read_excel("tabela_vendas_ZePequeno_original.xlsx", dtype = {"Valor_Venda": float}) 

# Inspeção das primeiras linhas
print(df.head())

# Verificação dos tipos de dados e nulos
print(df.info())

# Conversão coluna data para o formato datetime considerando dia primeiro (padrão brasileiro)
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

# Verifica novamente o tipo da coluna Data
print(f'Tipo coluna data após transformação: {df['Data'].dtypes}')

# Período a que se referem os dados
print(f"O período analisado corresponde ao período entre {df['Data'].dt.date.min()} e {df['Data'].dt.date.max()}")

# Total de registros (nº linhas)
print(df.shape)

# Verificação inconsistências de dados nas variáveis Região, Canal e Produto
# Região
print(df['Região'].value_counts())
print(df['Região'].unique().tolist()) # mesmas cidades com texto escrito de maneira diferente 

# Canal
print(df['Canal'].value_counts())
print(df['Canal'].unique().tolist())

# Produto
print(df['Produto'].value_counts())
print(df['Produto'].unique().tolist())

# Tratamento inconsistências variável Região
df['Região'] = df['Região'].str.lower().replace({'joinville' : 'Joinville', 
                                                 'blumenau': 'Blumenau',
                                                 'florianópolis': 'Florianópolis',
                                                 'sudeste': 'Sudeste',
                                                 'nordeste': 'Nordeste',
                                                 'sul': 'Sul',
                                                 'norte': 'Norte',
                                                 'rio de janeiro': 'Rio de Janeiro',
                                                 'são paulo': 'São Paulo',
                                                 'centro-oeste': 'Centro-Oeste',
                                                 'curitiba': 'Curitiba',

                                                })
print(f"Lista nomes regiões corrigidas: {df['Região'].unique().tolist()}")

# Tratamento inconsistências variável Canal
df['Canal'] = df['Canal'].str.lower().replace({'e-commerce' : 'E-commerce', 'loja física': 'Loja Física'})
print(f"Lista nomes dos canais de venda corrigidos: {df['Canal'].unique().tolist()}")

# Tratamento inconsistências variável Produto
df['Produto'] = df['Produto'].str.lower().replace({'paçoca' : 'Paçoca', 'rolhas': 'Rolhas'})
print(f"Lista nomes dos produtos corrigidos: {df['Produto'].unique().tolist()}")

# Criação variaveis Mês e Ano
df['Mês'] = df['Data'].dt.month
df['Ano'] = df['Data'].dt.year

print(df.head(2))

# Exportação dos dados tratados para o formato csv
df.to_csv("tabela_vendas_ZePequeno_limpa.csv", index= False)
