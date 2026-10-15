# Projeto 01 — Automação e Análise de Dados de Vendas

## 1. Objetivo

Desenvolver uma solução em Python para automatizar o carregamento, a validação, o tratamento, a consolidação e a análise de dados comerciais, gerando indicadores e relatórios para apoiar a tomada de decisão gerencial.

## 2. Contextualização e problema de negócio

Este projeto simula uma empresa varejista que comercializa diferentes produtos por múltiplos canais de venda e conta com vendedores distribuídos por regiões.

As informações comerciais estão armazenadas em arquivos separados e apresentam problemas de qualidade que precisam ser identificados antes da geração de indicadores confiáveis.

**Problema de negócio:** como automatizar a consolidação dos dados de vendas e identificar os principais fatores que influenciam o desempenho comercial da empresa?

## 3. Perguntas de negócio

- Como o faturamento evoluiu ao longo do período analisado?
- Quais produtos e categorias geraram maior receita?
- Quais canais de venda apresentaram melhor desempenho?
- Quais vendedores obtiveram os melhores resultados?
- Quais regiões concentraram o maior volume de vendas?
- Qual foi o impacto dos descontos sobre a receita?
- Qual é a margem estimada das vendas, considerando os custos dos produtos?

## 4. Escopo

- **Período:** janeiro a dezembro de 2025.
- **Fontes:** vendas, produtos e vendedores.
- **Atividades:** inspeção, validação, tratamento e integração dos dados; cálculo de indicadores; análise exploratória; elaboração de conclusões gerenciais; automação de relatórios.

O projeto utiliza dados simulados para fins educacionais e de portfólio. Não contempla modelos preditivos, machine learning ou integrações com sistemas externos nesta versão.

## 5. Tecnologias

- Python 3.14.5
- Pandas
- NumPy
- OpenPyXL
- Matplotlib
- Jupyter Notebook
- Git e GitHub

## 6. Estrutura do projeto

```text
projeto-01-automacao-relatorio-vendas/
├── dados/
│   ├── vendas.csv
│   ├── produtos.csv
│   └── vendedores.csv
├── notebooks/
│   └── projeto_01_analise_vendas.ipynb
├── .gitignore
├── requirements.txt
└── README.md
```

A estrutura representa os arquivos previstos para o repositório atual. Novos diretórios poderão ser adicionados conforme a evolução do projeto.

## 7. Fontes de dados

### Vendas — `vendas.csv`

Contém os registros das operações comerciais, com as seguintes colunas:

- `pedido_id`
- `data_venda`
- `cliente_id`
- `produto_id`
- `vendedor_id`
- `quantidade`
- `preco_unitario`
- `desconto`
- `canal_venda`
- `status`

### Produtos — `produtos.csv`

Contém o cadastro dos produtos:

- `produto_id`
- `produto`
- `categoria`
- `subcategoria`
- `custo`
- `preco_base`

### Vendedores — `vendedores.csv`

Contém o cadastro dos vendedores:

- `vendedor_id`
- `vendedor`
- `regiao`

## 8. Ambiente de desenvolvimento

O projeto foi desenvolvido no Windows 11, utilizando Python 3.14.5, gerenciado pelo `pyenv-win`, e um ambiente virtual isolado em `.venv/`.

O diretório `.venv/` não é versionado no Git.

### Instalação e execução

Clone o repositório:

```powershell
git clone https://github.com/ricardo-paganini/projeto-01-automacao-relatorio-vendas.git
cd projeto-01-automacao-relatorio-vendas
```

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Abra o Jupyter Notebook e execute `notebooks/projeto_01_analise_vendas.ipynb` utilizando o ambiente Python do projeto.

## 9. Progresso do projeto

### Etapas concluídas

- Configuração do ambiente Python e do ambiente virtual.
- Preparação e versionamento dos arquivos CSV.
- Criação e publicação do notebook principal.
- Documentação da contextualização, do problema de negócio, dos objetivos e da metodologia.
- Carregamento e inspeção inicial das fontes de dados.
- Conclusão do diagnóstico da qualidade dos dados.
- Identificação de valores ausentes, duplicidades, inconsistências e valores inválidos.
- Tratamento das 12 linhas totalmente duplicadas na base analítica, reduzindo o conjunto de 10.012 para 10.000 registros.

### Etapa em andamento

**Tratamento e padronização dos dados:** definição e implementação de regras para valores ausentes, status das vendas, quantidades inválidas e demais inconsistências identificadas no diagnóstico.

### Próximas etapas

1. Definir as regras de tratamento dos valores ausentes.
2. Padronizar status e categorias.
3. Avaliar e tratar registros com quantidades iguais a zero.
4. Validar a integridade e a consistência dos dados tratados.
5. Integrar as tabelas.
6. Calcular os indicadores comerciais.
7. Realizar a análise exploratória.
8. Elaborar conclusões e recomendações gerenciais.
9. Automatizar a geração do relatório.
## 10. Diagnóstico preliminar da qualidade dos dados

A avaliação da qualidade dos dados foi realizada sobre os arquivos de vendas, produtos e vendedores, com o objetivo de identificar problemas que possam comprometer a confiabilidade dos indicadores comerciais.

## 10. Diagnóstico da qualidade dos dados

A avaliação da qualidade dos dados foi realizada sobre os arquivos de vendas, produtos e vendedores, com o objetivo de identificar problemas que possam comprometer a confiabilidade dos indicadores comerciais.

### 10.1. Valores ausentes e duplicidades

A inspeção inicial identificou os seguintes problemas:

| Verificação | Resultado |
|---|---:|
| Registros de vendas originais | 10.012 |
| Linhas totalmente duplicadas identificadas | 12 |
| Registros após remoção das duplicidades | 10.000 |
| Duplicidades integrais restantes na base tratada | 0 |
| Valores ausentes em `vendedor_id` | 10 |
| Valores ausentes em `canal_venda` | 10 |
| Valores ausentes em `desconto` | 15 |

As tabelas de produtos e vendedores não apresentaram valores ausentes nem linhas totalmente duplicadas na inspeção inicial.

As 12 linhas totalmente duplicadas foram removidas da base analítica utilizando `drop_duplicates()`. O DataFrame original foi preservado, e a base de trabalho passou a ser `df_vendas_tratadas`.

### 10.2. Consistência e validade

As verificações complementares apresentaram os seguintes resultados:

| Verificação | Resultado |
|---|---|
| Quantidades iguais a zero ou negativas | 8 registros com quantidade zero foram apresentados na amostra |
| Descontos fora do intervalo de 0 a 100% | Nenhum registro identificado |
| Datas não interpretáveis | Nenhuma data identificada |
| Formatos de data | 10.012 registros no formato `AAAA-MM-DD` |
| Status com grafia divergente | 10 registros |
| Categorias com grafia divergente | 1 produto |
| Vendas com produto sem cadastro correspondente | Nenhuma identificada |
| Vendas com vendedor sem cadastro correspondente | Nenhuma identificada entre os identificadores não nulos |

As divergências de status envolvem variações de capitalização e acentuação. Na tabela de produtos, foi identificada a categoria `Eletronicos`, que difere da grafia `Eletrônicos`.

### 10.3. Coerência dos preços

Foram identificados 10.003 registros de vendas cujo `preco_unitario` difere do `preco_base` cadastrado para o produto.

Essa diferença não caracteriza, isoladamente, um erro. Os preços praticados podem refletir condições comerciais distintas do preço de referência. Por isso, não será realizada correção automática desses valores.

A análise de margem estimada deverá considerar o preço praticado, o desconto, o custo do produto e o status da venda, conforme as regras de negócio que serão definidas durante o tratamento dos dados.

### 10.4. Conclusão do diagnóstico

O diagnóstico identificou problemas de completude, duplicidade, padronização e validade que precisam ser considerados antes do cálculo dos indicadores comerciais.

O tratamento das duplicidades foi concluído e validado, com a remoção de 12 linhas integralmente duplicadas e a preservação dos dados originais.

As regras para tratar valores ausentes, quantidades iguais a zero, status das vendas e demais inconsistências ainda serão definidas e documentadas antes da aplicação das correções.

**Status:** diagnóstico da qualidade dos dados concluído. Tratamento e padronização dos dados em andamento.