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

   | Classificação | Faixa de valor           |
   |---------------|--------------------------|
   | Muito bom     | valor acima de R$ 2.500  |
   | Médio         | valor acima de R$ 2.000  |
   | Baixo         | até R$ 2.000             |

---

## Resultados e conclusões

### 1. Visão geral das vendas

- **Total de vendas:** 763 registros.
- **Receita total:** R$ 5.050.930,50.
- **Ticket médio por venda:** R$ 6.619,83.

### 2. Análise de receita por produto

Os produtos comercializados pela empresa são **Paçoca** e **Rolhas**. A distribuição da receita por produto foi a seguinte:

| Produto | Receita total | Participação na receita |
|---|---:|---:|
| Paçoca | R$ 3.839.682,40 | 76,02% |
| Rolhas | R$ 1.211.248,10 | 23,98% |
| **Total** | **R$ 5.050.930,50** | **100,00%** |

**Conclusão:** A receita gerada pela venda de paçoca foi aproximadamente **3,2 vezes maior** do que a receita obtida com a venda de rolhas. Além disso, a paçoca foi responsável por 76,02% da receita total, sendo o principal produto em termos de faturamento.

### 3. Análise de receita por canal de vendas

As vendas foram realizadas por dois canais: e-commerce e lojas físicas.

| Canal de vendas | Receita total | Participação na receita |
|---|---:|---:|
| E-commerce | R$ 3.060.238,00 | 60,59% |
| Loja Física | R$ 1.990.692,50 | 39,41% |
| **Total** | **R$ 5.050.930,50** | **100,00%** |

**Conclusão:** O e-commerce foi responsável pela maior parcela da receita, representando 60,59% do faturamento total. As lojas físicas contribuíram com os 39,41% restantes.

### 4. Classificação das vendas

Foram identificadas **152 vendas classificadas como muito boas**, o que corresponde a **19,92% do total de registros**.

Esse resultado permite identificar a participação das vendas de melhor desempenho dentro do conjunto analisado.

### 5. Análise de receita por região

A empresa realizou vendas em **11 regiões ou cidades**, conforme a lista abaixo:

- Joinville
- Blumenau
- Florianópolis
- Sudeste
- Nordeste
- Sul
- Norte
- Rio de Janeiro
- São Paulo
- Centro-Oeste
- Curitiba

#### Regiões com maior receita

As três regiões ou cidades com maior receita foram:

| Posição | Região/Cidade | Receita total |
|---:|---|---:|
| 1º | Blumenau | R$ 2.427.755,80 |
| 2º | Joinville | R$ 2.010.753,90 |
| 3º | Florianópolis | R$ 539.649,80 |

**Conclusão:** Blumenau apresentou a maior receita, seguida por Joinville e Florianópolis. Essas localidades se destacaram em relação às demais regiões atendidas pela empresa.

### 6. Distribuição das vendas muito boas por região

A distribuição das vendas classificadas como muito boas foi a seguinte:

| Região | Quantidade de vendas |
|---|---:|
| Joinville | 71 |
| Florianópolis | 43 |
| Blumenau | 32 |
| Nordeste | 2 |
| Rio de Janeiro | 2 |
| Centro-Oeste | 1 |
| Sudeste | 1 |
| **Total** | **152** |

**Conclusão:** Joinville concentrou o maior número de vendas muito boas, com 71 registros, seguida por Florianópolis, com 43, e Blumenau, com 32. Juntas, essas três localidades representam a maior parte das vendas classificadas nessa categoria.

---

## Estrutura do repositório

```
├── README.MD                        
├── analise_vendas.py                        # script em python com as análises
├── funcoes.py                               # função auxiliar calcular_receita()
├── tabela_vendas_ZePequeno_limpa.csv        # dados de vendas (já tratados)
├── tabela_vendas_ZePequeno_original.xlsx    # dados de vendas brutos(sem tratamento)
└── tratamento_dados.py                      # script em python com as transformações aplicadas aos dados
```
---

## Como executar

1. Instale o Python 3.12 ou superior e o pandas:
```bash
   pip install pandas
```
2. Deixe todos os arquivos na mesma pasta.
3. Rode o script:
```bash
   python analise_vendas.py
```


