import pandas as pd
from funcoes import calcular_receita

# Leitura dos dados
df = pd.read_csv("tabela_vendas_ZePequeno_limpa.csv") 

# Inspeção das primeiras linhas
# print(df.head())

# Verificação dos tipos dos dados
#print(df.info())

# Conversão coluna data para o formato datetime considerando dia primeiro (padrão brasileiro)
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

print("\nAnálise de vendas da empresa Zé Pequeno")

# Verificando data inicial e final do período analisado
print('\nPeríodo analisado')
print(f'Data início do período: {df['Data'].dt.date.min()}')
print(f'Data final do período: {df['Data'].dt.date.max()}')

# Total registros de vendas contabilizados no período
print(f'\nNo perído analisado foram contabilizados {len(df)} registros de vendas')

# Calcular receita total usando a função calcular_receita
receita_total = calcular_receita(df)
print(f'\nA receita total foi de R${receita_total:,.2f}')

# Ticket médio
venda_media = df['Valor_Venda'].mean()
print(f'O valor médio por venda foi R${venda_media:,.2f}')

# Produtos comercializados pela empresa ?
print(f'\nOs produtos comercializados pela empresa são: {df["Produto"].unique()}')

# Vericar a receita gerada por cada produto usando a função calcular_receita
receita_pacoca = calcular_receita(df, produto='Paçoca')
receita_rolhas = calcular_receita(df, produto='Rolhas')

# Qual foi a receita de paçoca e quanto ela representa no total
print(f'\nA receita de paçoca foi de R${receita_pacoca:,.2f} e representa {receita_pacoca/receita_total:.2%} do total')

# Qual foi a receita de rolhas e quanto ela representa no total
print(f'Já a receita de rolhas foi de R${receita_rolhas:,.2f} e representa {receita_rolhas/receita_total:.2%} do total')

# Receita paçoca em relação a receita de rolhas
print(f'A receita de vendas gerada por paçoca representa {receita_pacoca/receita_rolhas:.1f} vezes a receita de rolhas')

# Canais de origem das receitas de venda
print(f'\nOs canais que originaram as vendas são: {df["Canal"].unique()}')

# Levantamento da receita de vendas por canal usando a função calcular receita
receita_ecommerce = calcular_receita(df, canal='E-commerce')
receita_loja_fisica = calcular_receita(df, canal='Loja Física')
print(f'A receita proveniente do e-commerce foi de R${receita_ecommerce:,.2f} e representa {receita_ecommerce/receita_total:.2%} do total')
print(f'E a receita das lojas físicas foi de R${receita_loja_fisica:,.2f} e representa {receita_loja_fisica/receita_total:.2%} do total')

# Análise distribuição valores das vendas para embasar a classificação das vendas muito boas
#print(f['Valor_Venda'].describe())
valor_muito_bom = 2500
valor_medio = 2000
df['classificacao_venda'] = df['Valor_Venda'].apply(lambda x: 'Muito bom' if x > valor_muito_bom else ('Médio' if x > valor_medio else 'Baixo')) 

# df somente com vendas muito boas
df_melhores_vendas = df[df['classificacao_venda'] == 'Muito bom']
total_melhores_vendas = len(df_melhores_vendas)
tota_geral =len(df)
print(f'\nForam realizadas {total_melhores_vendas} vendas muito boas e representam {total_melhores_vendas/tota_geral:.2%} do total')

# Quantas e quais são as regiões atendidas?
print(f'\nNúmero total de regiões atendidas: {len(df['Região'].unique())}')
print(f'\nNomes das regiões/cidades atendidas:')
for regiao in df["Região"].unique():
    print(regiao)

# # E quais das regiões geraram mais receita?
receita_por_regiao= df.groupby('Região')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False)
top_3 = receita_por_regiao.head(3)

print('\nE as três com maiores receitas foram:')

for indice, linha in top_3.iterrows():
    print(f'{linha["Região"]}: R$ {linha["Valor_Venda"]:,.2f}')

# E como se distribuem as melhores vendas entre as regiões?
print('\nDistribuição das melhores vendas por região:')
print(df_melhores_vendas.groupby('Região')['Valor_Venda'].count().sort_values(ascending=False))

