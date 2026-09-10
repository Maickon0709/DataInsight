# DataInsight — Sales Analytics

## 📊 Sobre o projeto

**DataInsight** é um projeto de análise de dados desenvolvido em Python como projeto final do **CS50's Introduction to Programming with Python (CS50P)**.

O projeto utiliza dados reais de vendas de uma empresa de varejo online para demonstrar como Python pode ser utilizado para **carregar, limpar, analisar e visualizar dados**.

O objetivo é transformar dados brutos em informações que ajudem a compreender o desempenho das vendas.

---

## 🎯 Objetivos

O DataInsight busca responder perguntas como:

- Qual foi o faturamento total?
- Quantos produtos foram vendidos?
- Quantas transações foram realizadas?
- Qual foi o ticket médio?
- Quais produtos geraram mais faturamento?
- Quais produtos foram vendidos em maior quantidade?
- Quais países geraram mais faturamento?
- Como o faturamento variou ao longo dos meses?

---

## 🗃️ Dataset

O projeto utiliza o dataset **Online Retail**, disponibilizado pelo **UCI Machine Learning Repository**.

Os dados representam transações de uma empresa de varejo online do Reino Unido realizadas entre **dezembro de 2010 e dezembro de 2011**.

O conjunto original possui **541.909 registros** e 8 colunas:

| Coluna | Descrição |
|---|---|
| `InvoiceNo` | Número da transação |
| `StockCode` | Código do produto |
| `Description` | Descrição do produto |
| `Quantity` | Quantidade de produtos |
| `InvoiceDate` | Data e horário da transação |
| `UnitPrice` | Preço unitário |
| `CustomerID` | Identificação do cliente |
| `Country` | País do cliente |

---

## 🧹 Tratamento dos dados

Antes da análise, os dados passam por uma etapa de limpeza.

O projeto:

1. Remove registros duplicados.
2. Remove notas fiscais de vendas canceladas.
3. Remove registros com quantidade inválida.
4. Remove registros com preço inválido.
5. Remove registros sem descrição do produto.
6. Cria a coluna `TotalPrice`.

O valor total de cada registro é calculado por:

```text
TotalPrice = Quantity × UnitPrice
```

---

## 📈 Indicadores

Após a limpeza, o DataInsight calcula:

- Faturamento total;
- Quantidade total de produtos vendidos;
- Número de transações;
- Ticket médio;
- Top 10 produtos por faturamento;
- Top 10 produtos por quantidade;
- Top 10 países por faturamento;
- Faturamento mensal.

O ticket médio é calculado por:

```text
Ticket médio = Faturamento total ÷ Número de transações
```

---

## 📊 Visualizações

O projeto utiliza **Matplotlib** para gerar gráficos automaticamente.

São gerados:

- Faturamento mensal;
- Top 10 produtos por faturamento;
- Top 10 países por faturamento.

Os gráficos são salvos na pasta:

```text
charts/
```

---

## 🏗️ Estrutura do projeto

```text
DataInsight/
│
├── data/
│   └── Online Retail.xlsx
│
├── charts/
│   ├── monthly_revenue.png
│   ├── top_products.png
│   └── country_revenue.png
│
├── project.py
├── test_project.py
├── requirements.txt
└── README.md
```

---

## 📁 Arquivos

### `project.py`

Arquivo principal do projeto. Contém as funções responsáveis por carregar, limpar e analisar os dados, gerar os gráficos e executar o programa.

### `test_project.py`

Contém os testes automatizados feitos com **Pytest** para verificar o carregamento, a limpeza e os cálculos da análise.

### `requirements.txt`

Lista as bibliotecas externas necessárias para executar o projeto.

### `README.md`

Documentação do projeto.

### `data/Online Retail.xlsx`

Dataset utilizado na análise.

### `charts/`

Pasta onde os gráficos gerados pelo programa são armazenados.

---

## 🧩 Organização do código

O projeto foi dividido em funções para separar responsabilidades:

- `load_data()` — carrega o arquivo Excel;
- `clean_data()` — prepara e limpa os dados;
- `analyze_data()` — calcula os principais indicadores;
- `create_charts()` — cria e salva os gráficos;
- `main()` — coordena a execução do programa.

Essa organização facilita a leitura, manutenção e realização de testes.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas** — manipulação e análise de dados
- **Matplotlib** — criação de gráficos
- **OpenPyXL** — leitura de arquivos Excel
- **Pytest** — testes automatizados

---

## ▶️ Como executar

### Instalar as dependências

No terminal, dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

### Executar o projeto

```bash
python project.py
```

O programa irá:

1. Carregar o dataset;
2. Limpar os dados;
3. Calcular os indicadores;
4. Exibir os resultados no terminal;
5. Gerar os gráficos na pasta `charts`.

### Executar os testes

```bash
pytest
```

---

## 📋 Fluxo do projeto

```text
Online Retail.xlsx
        ↓
   load_data()
        ↓
   clean_data()
        ↓
  analyze_data()
        ↓
 create_charts()
        ↓
Resultados + Gráficos
```

---

## 🎥 Vídeo de demonstração

**Vídeo:**  
INSIRA AQUI O LINK DO SEU VÍDEO NO YOUTUBE

O vídeo apresentará a execução do programa, sua estrutura, as principais funcionalidades e os resultados obtidos.

---

## 👨‍💻 Autor

**Maickon Santos**

Estudante de Análise e Desenvolvimento de Sistemas.

Projeto desenvolvido para o **CS50's Introduction to Programming with Python (CS50P)**.

---

## 📚 Fonte dos dados

**UCI Machine Learning Repository — Online Retail Dataset**

O dataset é disponibilizado sob a licença **CC BY 4.0**.
