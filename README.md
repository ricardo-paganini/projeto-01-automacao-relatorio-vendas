# Projeto 01 — Automação de Relatório de Vendas

## Objetivo

Desenvolver uma solução em Python para automatizar o carregamento, tratamento, consolidação e análise de dados de vendas, gerando informações para apoiar a tomada de decisão gerencial.

## Descrição

Este projeto simula um cenário empresarial no qual dados de vendas, produtos e vendedores precisam ser tratados e consolidados para geração de um relatório gerencial.

Os dados foram criados especificamente para o projeto e contêm problemas controlados de qualidade, como valores ausentes, duplicidades, inconsistências de formato e valores inválidos.

O objetivo é reproduzir, de forma prática, etapas comuns de um projeto de análise de dados utilizando Python.

## Tecnologias

- Python 3.14.5
- Pandas
- NumPy
- OpenPyXL
- Matplotlib
- Jupyter Notebook
- Git / GitHub

## Estrutura do projeto

```text
projeto-01-automacao-relatorio-vendas/
│
├── dados/
│   ├── vendas.csv
│   ├── produtos.csv
│   └── vendedores.csv
├── .gitignore
├── preparar_dados.py
├── requirements.txt
└── README.md
```

## Dados

O projeto utiliza três conjuntos de dados:

### Vendas

Contém as transações comerciais realizadas durante o período analisado.

Principais informações:

- pedido
- data da venda
- cliente
- produto
- vendedor
- quantidade
- preço unitário
- desconto
- canal de venda
- status da venda

### Produtos

Contém informações cadastrais dos produtos:

- produto
- categoria
- subcategoria
- custo
- preço base

### Vendedores

Contém informações dos vendedores:

- vendedor
- região

## Ambiente de desenvolvimento

O projeto utiliza um ambiente virtual Python isolado criado com `venv`.

Versão utilizada:

```text
Python 3.14.5
```

O Python é gerenciado pelo `pyenv-win`.

O ambiente virtual está localizado em:

```text
.venv/
```

O diretório `.venv` não é versionado no Git.

## Como executar

Clone o repositório e entre no diretório do projeto.

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Status do projeto

Em desenvolvimento.