# Análise de Vendas – Zé Pequeno Paçocas e Rolhas Ltda

Mini projeto de análise de dados em Python com pandas.

A **Zé Pequeno Paçocas e Rolhas Ltda** é uma empresa fictícia que exemplifica a **economia circular**: ela produz paçoca de amendoim e reaproveita a casca do amendoim para fabricar rolhas.


---

## Perguntas respondidas

1. Quantas vendas foram registradas no período analisado?
2. Qual foi a receita total e o valor médio por venda (ticket médio)?
3. Quanto cada um dos produtos vendidos representa na receita?
4. Por qual canal (E-commerce ou Loja Física) as vendas acontecem e qual a participação de cada um?
5. Quantas vendas podem ser classificadas como "muito boas"?
6. Quais regiões são atendidas, quais geram mais receita e onde estão as melhores vendas?

---

## Estrutura do projeto

```
├── historia_vendas.py                       # script em python com as análises
├── funcoes.py                               # função auxiliar calcular_receita()
├── tabela_vendas_ZePequeno_limpa.csv        # dados de vendas (já tratados)
└── tabela_vendas_ZePequeno_original.xlsx    # dados de vendas (já tratados)
```

---

## 📋 Sobre os dados

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

## ⚙️ Como o script funciona

1. **Leitura:** carrega o CSV com `pandas`.
2. **Tratamento da data:** converte a coluna `Data` para `datetime`, usando `dayfirst=True` porque o formato brasileiro é dia/mês/ano.
3. **Métricas gerais:** período, número de registros, receita total e ticket médio.
4. **Receita por produto e por canal:** usa a função `calcular_receita()` com filtros opcionais (`produto=` e `canal=`) e calcula a participação de cada um no total.
5. **Classificação das vendas:** cada venda recebe um rótulo conforme o valor:

   | Classificação | Regra                    |
   |---------------|--------------------------|
   | Muito bom     | valor acima de R$ 2.500  |
   | Médio         | valor acima de R$ 2.000  |
   | Baixo         | demais casos             |

6. **Análise por região:** lista as regiões atendidas, o top 3 em receita e a distribuição das vendas "muito boas".

---

## ▶️ Como executar

1. Instale o Python 3.12 ou superior e o pandas:
```bash
   pip install pandas
```
2. Deixe os quatro arquivos na mesma pasta.
3. Rode o script:
```bash
   python analise_vendas.py
```

---

## Tecnologias usadas

- Python
- pandas

