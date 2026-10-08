# Análise de Vendas – Zé Pequeno Paçocas e Rolhas Ltda

Mini projeto de análise de dados em Python com pandas.

A **Zé Pequeno Paçocas e Rolhas Ltda** é uma empresa fictícia que exemplifica a **economia circular**: ela produz paçoca de amendoim e reaproveita a casca do amendoim para fabricar rolhas.

---

## Perguntas de negócio

1. Quantas vendas foram registradas no período analisado?
2. Qual foi a receita total e o valor médio por venda (ticket médio)?
3. Qual dos produtos vendidos tem a maior participação na receita?
4. Por quais canais as vendas foram realizadas e qual a participação de cada um?
5. Quantas são as vendas classificadas como "muito boas"?
6. Quantas e quais são as regiões atendidas, quais geram mais receita e onde estão as melhores vendas?

---

## Fonte de dados

Os dados foram obtidos a partir da tabela de vendas `tabela_vendas_ZePequeno_original.xlsx` a qual continha 763 registros ao todo.

---

## Dicionário de dados

| Coluna        | Descrição                                      |
|---------------|------------------------------------------------|
| `Data`        | Data da venda (formato dia/mês/ano)            |
| `Região`      | Região ou cidade da venda                      |
| `Canal`       | Canal de venda: E-commerce ou Loja Física      |
| `Produto`     | Produto vendido: Paçoca ou Rolhas              |
| `Valor_Venda` | Valor da venda em reais (R$)                   |
| `Mês`         | Mês da venda                                   |
| `Ano`         | Ano da venda                                   |

---

## Ferramentas e tecnologias utilizadas

- Visual Studio Code
- Python
- Pandas

---

## Critério utilizado para a classificação e identificação das melhores vendas

As vendas foram classificadas em três faixas, de acordo com o valor de cada uma (`Valor_Venda`). Os valores de corte foram definidos após analisar a distribuição dos dados com o método `.describe()` do pandas, que mostra média, mediana, quartis, mínimo e máximo.

   | Classificação | Regra                    |
   |---------------|--------------------------|
   | Muito bom     | valor acima de R$ 2.500  |
   | Médio         | valor acima de R$ 2.000  |
   | Baixo         | demais casos             |

---

## Resultados e conclusões

- No perído analisado foram contabilizados 763 registros de vendas
- A receita total foi de R$5,050,930.50
- O valor médio por venda foi R$6,619.83
- Os produtos comercializados pela empresa são: ['Paçoca' 'Rolhas']
- A receita de paçoca foi de R$3,839,682.40 e representa 76.02% do total
- Já a receita de rolhas foi de R$1,211,248.10 e representa 23.98% do total
- A receita de vendas gerada por paçoca representa 3.2 vezes a receita de rolhas

- Os canais que originaram as vendas são: ['E-commerce' 'Loja Física']
- A receita proveniente do e-commerce foi de R$3,060,238.00 e representa 60.59% do total
- E a receita das lojas físicas foi de R$1,990,692.50 e representa 39.41% do total

- Foram realizadas 152 vendas muito boas e representam 19.92% do total

- Número total de regiões atendidas: 11

 - Nomes das regiões/cidades atendidas:
Joinville,
Blumenau,
Florianópolis,
Sudeste,
Nordeste,
Sul,
Norte,
Rio de Janeiro,
São Paulo,
Centro-Oeste,
Curitiba

- E as três com maiores receitas foram:
Blumenau: R$ 2,427,755.80
Joinville: R$ 2,010,753.90
Florianópolis: R$ 539,649.80

- Distribuição das melhores vendas por região:
Região
Joinville         71
Florianópolis     43
Blumenau          32
Nordeste           2
Rio de Janeiro     2
Centro-Oeste       1
Sudeste            1

---

## Estrutura do repositório

```
├── analise_vendas.py                       # script em python com as análises
├── funcoes.py                               # função auxiliar calcular_receita()
├── tabela_vendas_ZePequeno_limpa.csv        # dados de vendas (já tratados)
└── tabela_vendas_ZePequeno_original.xlsx    # dados de vendas brutos(sem tratamento)
```
---

## Como executar

1. Instale o Python 3.12 ou superior e o pandas:
```bash
   pip install pandas
```
2. Deixe os quatro arquivos na mesma pasta.
3. Rode o script:
```bash
   python analise_vendas.py
```

