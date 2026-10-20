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

### 4.1. Critérios de sucesso do projeto

A fase de Entendimento do Negócio, conforme a metodologia CRISP-DM, estabeleceu os seguintes critérios de sucesso:

1. **Confiabilidade dos dados:** identificar, documentar e tratar inconsistências relevantes, preservando os arquivos originais.
2. **Integração das fontes:** consolidar os dados de vendas, produtos e vendedores, verificando a integridade dos relacionamentos.
3. **Indicadores comerciais:** calcular faturamento, evolução mensal, desempenho por produto, categoria, canal, vendedor e região.
4. **Descontos:** avaliar o impacto dos descontos sobre a receita, considerando as regras de negócio definidas.
5. **Margem estimada:** calcular a margem com base no preço efetivamente praticado, nos descontos aplicados e nos custos cadastrados dos produtos.
6. **Validação:** conferir os cálculos e documentar as regras utilizadas para inclusão ou exclusão de registros.
7. **Automação:** desenvolver um processo reproduzível para gerar relatórios gerenciais a partir dos arquivos de entrada.
8. **Documentação e versionamento:** manter o README.md atualizado e registrar cada etapa no Git e GitHub.

### 4.2. Regras de negócio a definir

Antes do cálculo dos indicadores, deverão ser estabelecidas e documentadas as seguintes regras:

- Quais status de venda serão considerados no faturamento.
- Como tratar vendas canceladas, devolvidas ou com informações inconsistentes.
- Como interpretar o campo `desconto` e aplicá-lo aos cálculos.
- Como tratar quantidades iguais a zero.
- Como lidar com valores ausentes e registros duplicados.
- Como calcular o custo total e a margem estimada.

Essas definições serão validadas durante as etapas de entendimento e preparação dos dados, antes da geração dos indicadores definitivos.

**Status da fase CRISP-DM:** Entendimento do Negócio — escopo e critérios de sucesso aprovados.

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

### Validação do ambiente

Em 17/10/2026, o ambiente virtual foi validado no Windows PowerShell.

- **Python:** 3.14.5
- **Pandas:** 3.0.6
- **Dependências:** instaladas conforme o arquivo `requirements.txt`.
- **Integridade:** `python -m pip check` executado sem dependências quebradas.
- **Reprodutibilidade:** a saída de `python -m pip freeze` corresponde às dependências declaradas em `requirements.txt`.

O ambiente está preparado para iniciar o desenvolvimento analítico do projeto.

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
- Identificação inicial de valores ausentes, duplicidades e tipos de dados.
- Documentação das perguntas de negócio no notebook principal.

### Etapa em andamento

**Entendimento do Negócio:** escopo, perguntas de negócio e critérios de sucesso definidos. As regras de negócio para o cálculo dos indicadores ainda precisam ser validadas.

### Próximas etapas

1. Concluir o entendimento e o diagnóstico dos dados.
2. Definir e documentar as regras de tratamento.
3. Tratar e padronizar as informações.
4. Integrar as tabelas.
5. Calcular os indicadores comerciais.
6. Realizar a análise exploratória.
7. Elaborar conclusões e recomendações gerenciais.
8. Automatizar a geração do relatório.

## 10. Diagnóstico preliminar da qualidade dos dados

A avaliação da qualidade dos dados foi realizada sobre os arquivos de vendas, produtos e vendedores, com o objetivo de identificar problemas que possam comprometer a confiabilidade dos indicadores comerciais.

### 10.1. Valores ausentes e duplicidades

A inspeção inicial identificou os seguintes problemas:

| Verificação | Resultado |
|---|---:|
| Registros de vendas | 10.012 |
| Linhas totalmente duplicadas em vendas | 12 |
| Valores ausentes em `vendedor_id` | 10 |
| Valores ausentes em `canal_venda` | 10 |
| Valores ausentes em `desconto` | 15 |

As tabelas de produtos e vendedores não apresentaram valores ausentes nem linhas totalmente duplicadas na inspeção inicial.

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

A análise de margem estimada deverá considerar o preço praticado, o desconto, o custo do produto e o status da venda, conforme as regras de negócio que serão definidas na etapa de tratamento.

### 10.4. Conclusão do diagnóstico

O diagnóstico identificou problemas de completude, duplicidade, padronização e validade que precisam ser considerados antes do cálculo dos indicadores comerciais.

Os resultados foram registrados sem modificar os dados originais. As regras para tratar valores ausentes, duplicidades, quantidades iguais a zero e status das vendas serão definidas na próxima etapa, com critérios explícitos e rastreáveis.

**Status:** diagnóstico da qualidade dos dados concluído. Tratamento e padronização dos dados pendentes.
