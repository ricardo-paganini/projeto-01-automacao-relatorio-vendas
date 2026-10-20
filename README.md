# Projeto 01 — Retail Sales Analytics Platform

## 1. Objetivo

Desenvolver uma plataforma analítica de vendas que integre engenharia e análise de dados, desde a ingestão e validação dos arquivos de origem até a disponibilização de indicadores comerciais em dashboards interativos no Databricks.

O projeto tem como objetivo demonstrar competências em Python, SQL, PySpark, Databricks, qualidade de dados, análise de indicadores, documentação técnica e versionamento com Git e GitHub.

## 2. Contextualização e problema de negócio

Este projeto simula uma empresa varejista que comercializa diferentes produtos por múltiplos canais de venda e conta com vendedores distribuídos por regiões.

As informações comerciais estão organizadas em arquivos que precisam ser consolidados, validados e preparados para gerar indicadores confiáveis.

Problemas como duplicidades, valores ausentes, inconsistências de preenchimento e regras de cálculo inadequadas podem comprometer a qualidade das análises e prejudicar a tomada de decisão.

**Problema de negócio:** como transformar dados comerciais brutos em informações confiáveis, utilizando um processo reproduzível de engenharia e análise de dados, para compreender o desempenho das vendas e apoiar decisões gerenciais?

A solução proposta utilizará o Databricks para processamento, armazenamento, consultas SQL, visualização e compartilhamento dos resultados.

A base de dados é fictícia e foi desenvolvida para fins educacionais e de portfólio. Portanto, as análises representarão um cenário simulado, e não o desempenho de uma empresa real.

## 3. Perguntas de negócio

O projeto deverá responder às seguintes perguntas:

- Como o faturamento evolui ao longo do período analisado?
- Quais produtos e categorias concentram o maior faturamento?
- Quais canais de venda apresentam maior participação nas vendas?
- Como o desempenho comercial se distribui entre os vendedores?
- Quais regiões apresentam maior volume de vendas?
- Qual é o impacto dos descontos sobre a receita?
- É possível calcular lucro e margem de forma confiável com os dados disponíveis?
- Quais problemas de qualidade podem comprometer os indicadores?
- Como estruturar um pipeline reproduzível para disponibilizar os dados para análise?
- Como disponibilizar e compartilhar dashboards interativos no Databricks?

As respostas dependerão da estrutura da base, das regras de negócio e da validação dos resultados.

## 4. Escopo

- **Segmento:** varejo.
- **Período dos dados:** janeiro a dezembro de 2025, conforme a base recebida.
- **Fonte principal:** arquivo fictício `dados_projeto_01.xlsx`.
- **Planilhas:** vendas, produtos e vendedores.
- **Processamento:** Python, pandas, PySpark e Databricks.
- **Armazenamento:** camadas Bronze, Silver e Gold.
- **Análise:** consultas SQL e indicadores comerciais.
- **Visualização:** dashboards nativos do Databricks.
- **Versionamento:** Git e GitHub.
- **Documentação:** Jupyter Notebook e README.md.

O escopo inclui a inspeção da estrutura, a validação da qualidade, a definição de regras de tratamento, a integração das tabelas, o cálculo de indicadores e a construção de dashboards para análise do desempenho comercial.

O compartilhamento dos dashboards será realizado conforme os recursos e as permissões disponíveis no workspace do Databricks.

Não fazem parte do escopo inicial o desenvolvimento de modelos preditivos, machine learning, processamento em streaming ou infraestrutura complexa de produção.

## 5. Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python | Análise exploratória, validações e automação |
| pandas | Leitura e análise inicial dos arquivos |
| PySpark | Transformação e processamento de dados |
| Databricks | Ambiente de engenharia, análise e armazenamento |
| SQL | Consultas analíticas e cálculo de indicadores |
| Databricks AI/BI Dashboards | Visualização e compartilhamento dos resultados |
| Jupyter Notebook | Registro das análises e evidências |
| Git | Controle de versão |
| GitHub | Hospedagem do código e documentação |

A utilização efetiva dos recursos do Databricks dependerá da configuração e das permissões disponíveis no workspace.

## 6. Estrutura do projeto

A estrutura será organizada progressivamente, preservando os arquivos existentes e incorporando novos componentes conforme a necessidade.

```text
projeto-01-automacao-relatorio-vendas/
├── dados/
│   └── dados_projeto_01.xlsx
├── notebooks/
│   └── projeto_01_analise_vendas.ipynb
├── .gitignore
├── requirements.txt
└── README.md
```

A estrutura apresentada é a organização prevista para o projeto. Os caminhos e diretórios deverão ser conferidos com a estrutura efetivamente existente no repositório antes de serem considerados definitivos.

Novos diretórios poderão ser adicionados para organizar scripts, consultas SQL, configurações e documentação técnica, caso sejam necessários.

## 7. Fontes de dados

### 7.1. Vendas

**Arquivo de origem:** `dados_projeto_01.xlsx`  
**Planilha:** `vendas`

Contém os registros das operações comerciais, com campos relacionados a:

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

A estrutura definitiva, os tipos de dados e a granularidade serão documentados durante a etapa de entendimento dos dados.

### 7.2. Produtos

**Arquivo de origem:** `dados_projeto_01.xlsx`  
**Planilha:** `produtos`

Contém informações cadastrais dos produtos, incluindo:

- `produto_id`
- `produto`
- `categoria`
- `subcategoria`
- `custo`
- `preco_base`

Esses campos poderão apoiar análises por produto e categoria, além de cálculos de rentabilidade, desde que as regras de negócio sejam devidamente estabelecidas.

### 7.3. Vendedores

**Arquivo de origem:** `dados_projeto_01.xlsx`  
**Planilha:** `vendedores`

Contém informações cadastrais dos vendedores, incluindo:

- `vendedor_id`
- `vendedor`
- `regiao`

Os relacionamentos com a tabela de vendas serão verificados antes da integração dos dados.

## 8. Ambiente de desenvolvimento

O desenvolvimento local utiliza Windows, Python e um ambiente virtual isolado em `.venv/`.

O ambiente virtual deve ser mantido fora do versionamento do Git.

### Instalação e execução

Clone o repositório:

```powershell
git clone https://github.com/ricardo-paganini/projeto-01-automacao-relatorio-vendas.git
cd projeto-01-automacao-relatorio-vendas
```

Crie e ative o ambiente virtual, caso ainda não exista:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências registradas no projeto:

```powershell
python -m pip install -r requirements.txt
```

Abra o notebook `projeto_01_analise_vendas.ipynb` no VS Code ou Jupyter Notebook, utilizando o interpretador Python do ambiente virtual.

A preparação e o processamento dos dados no Databricks serão realizados no workspace configurado para o projeto. O ambiente local e o workspace Databricks são componentes distintos e deverão ser configurados conforme a necessidade de cada etapa.

## 9. Progresso do projeto

O projeto seguirá a metodologia CRISP-DM, com execução e validação de cada fase antes do avanço para a próxima.

### Etapa 1 — Entendimento do negócio

**Objetivo:** definir o contexto, o problema, os objetivos, as perguntas analíticas, os indicadores previstos e o escopo técnico.

**Situação:** escopo aprovado. A documentação revisada deverá ser inserida no notebook e no README, validada e publicada no GitHub.

### Etapa 2 — Entendimento dos dados

**Objetivo:** investigar a estrutura, a granularidade, os relacionamentos, os tipos de dados e os problemas de qualidade.

**Situação:** aguardando a conclusão formal da Etapa 1.

### Etapa 3 — Preparação dos dados

**Objetivo:** definir e aplicar regras justificadas para tratar inconsistências e preparar as tabelas para análise.

**Situação:** não iniciada nesta sequência de trabalho.

### Etapa 4 — Modelagem

**Objetivo:** construir o pipeline de dados, organizar as camadas Bronze, Silver e Gold e desenvolver as consultas analíticas.

**Situação:** não iniciada nesta sequência de trabalho.

### Etapa 5 — Avaliação

**Objetivo:** validar as transformações, os relacionamentos, os indicadores e a consistência dos resultados.

**Situação:** não iniciada nesta sequência de trabalho.

### Etapa 6 — Implantação

**Objetivo:** publicar os dashboards no Databricks, validar o compartilhamento, finalizar a documentação e verificar o repositório.

**Situação:** não iniciada nesta sequência de trabalho.

## 10. Critérios de sucesso e qualidade

O projeto será considerado concluído quando:

1. A origem, a estrutura e a granularidade dos dados estiverem documentadas.
2. Os problemas de qualidade forem identificados e tratados com regras justificadas.
3. Os relacionamentos entre as tabelas forem verificados.
4. As transformações forem reproduzíveis e acompanhadas de testes.
5. As camadas Bronze, Silver e Gold estiverem funcionais e documentadas.
6. Os indicadores comerciais apresentarem cálculos consistentes e verificáveis.
7. Os dashboards responderem às perguntas de negócio definidas.
8. As visualizações e os filtros forem testados.
9. O compartilhamento dos dashboards for validado conforme as permissões disponíveis.
10. As limitações dos dados fictícios estiverem documentadas.
11. O README refletir o estado real do projeto.
12. As alterações estiverem versionadas e a publicação no GitHub estiver verificada.

Nenhuma atividade será considerada concluída apenas porque o código foi escrito. A conclusão dependerá da execução, da validação e do registro das evidências correspondentes.

### Premissas e limitações

- Os dados utilizados são fictícios.
- Os resultados não representam uma empresa real.
- As regras de negócio deverão ser confirmadas durante a análise.
- A existência de custos e preços de referência não garante, por si só, que seja possível calcular lucro e margem de forma confiável.
- Nenhuma correção será aplicada sem justificativa e validação.
- A disponibilidade de recursos de processamento, armazenamento e compartilhamento dependerá do workspace Databricks.
- O estado das etapas deverá ser atualizado conforme as atividades forem efetivamente executadas e validadas.