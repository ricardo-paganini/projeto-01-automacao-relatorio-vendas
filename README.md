# Projeto 01 — Retail Sales Analytics Platform

## 1. Objetivo

Desenvolver uma solução de análise e engenharia de dados utilizando o Databricks Free, com Python, PySpark e SQL, para transformar dados comerciais em informações confiáveis para apoiar a tomada de decisão.

O projeto será organizado em camadas de dados, com validações de qualidade, tabelas analíticas e dashboards nativos do Databricks.

## 2. Contextualização e problema de negócio

Este projeto simula uma empresa varejista que comercializa produtos por diferentes canais de venda e possui vendedores distribuídos por regiões.

Os dados comerciais estão disponíveis em fontes separadas e apresentam problemas de qualidade que precisam ser investigados antes do cálculo dos indicadores.

**Problema de negócio:** como estruturar e analisar os dados comerciais para compreender o desempenho das vendas, dos produtos, dos canais e dos vendedores?

## 3. Perguntas de negócio

- Como a receita evoluiu ao longo de 2025?
- Quais produtos e categorias geraram maior receita?
- Quais canais de venda apresentaram melhor desempenho?
- Quais vendedores obtiveram os melhores resultados?
- Quais regiões concentraram o maior volume de vendas?
- Qual foi o impacto dos descontos sobre a receita?
- Qual é a margem estimada das vendas, considerando os custos dos produtos?

As respostas dependerão da validação dos dados e da definição explícita das regras de negócio.

## 4. Escopo

### Incluído

- Ingestão dos dados no Databricks.
- Inspeção e validação das fontes.
- Diagnóstico e tratamento da qualidade dos dados.
- Organização das camadas Bronze, Silver e Gold.
- Transformações com PySpark e consultas SQL.
- Integração das tabelas de vendas, produtos e vendedores.
- Cálculo de indicadores comerciais.
- Análise exploratória e conclusões gerenciais.
- Construção de dashboards nativos do Databricks.
- Documentação técnica e versionamento no GitHub.

### Não incluído nesta versão

- Modelos preditivos e machine learning.
- Integrações com sistemas corporativos externos.
- Implantação em ambiente produtivo empresarial.
- Uso de serviços pagos ou recursos que não estejam disponíveis na edição gratuita.

## 5. Dados de origem

O projeto utiliza dados fictícios para fins educacionais e de portfólio.

| Fonte | Registros identificados | Colunas |
|---|---:|---:|
| Vendas | 10.012 | 10 |
| Produtos | 20 | 6 |
| Vendedores | 10 | 3 |

Os quantitativos acima correspondem à inspeção inicial realizada localmente e deverão ser reproduzidos após a ingestão no Databricks.

### Vendas

Contém identificador do pedido, data, cliente, produto, vendedor, quantidade, preço unitário, desconto, canal e status.

### Produtos

Contém identificador, nome, categoria, subcategoria, custo e preço de referência.

### Vendedores

Contém identificador, nome e região do vendedor.

## 6. Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Databricks Free | Ambiente principal de desenvolvimento e análise |
| Python | Linguagem para processamento e validações |
| PySpark | Transformação e processamento dos dados com Spark |
| SQL | Consultas e cálculo de indicadores |
| Delta Lake | Armazenamento de tabelas analíticas, conforme os recursos disponíveis |
| Unity Catalog | Organização e governança de dados, conforme os recursos disponíveis |
| Databricks AI/BI Dashboards | Visualização e apresentação dos indicadores |
| Git e GitHub | Versionamento do código e documentação |

As funcionalidades efetivamente utilizadas serão confirmadas no workspace antes da implementação.

## 7. Arquitetura proposta

### Bronze — dados de origem

Armazenar os dados ingeridos preservando o conteúdo original e documentando a origem e a execução da ingestão.

### Silver — dados tratados

Aplicar regras validadas de qualidade, padronização, tipagem e integridade dos relacionamentos. Os tratamentos serão documentados e testados.

### Gold — dados analíticos

Disponibilizar tabelas preparadas para responder às perguntas de negócio e alimentar os indicadores e dashboards.

A implementação de cada camada dependerá dos recursos de armazenamento e catálogo disponíveis na edição gratuita.

## 8. Estrutura proposta do repositório

```text
projeto-01-automacao-relatorio-vendas/
├── README.md
├── notebook/
│   ├── projeto_01_analise_vendas
└── docs/
    ├── arquitetura.md
    └── dashboards.md
```

Essa estrutura é uma proposta. Os arquivos serão criados ou reorganizados conforme a implementação e a validação de cada etapa.

## 9. Metodologia

O projeto seguirá o CRISP-DM, adaptado ao escopo:

1. Entendimento do negócio.
2. Entendimento dos dados.
3. Preparação dos dados.
4. Modelagem analítica.
5. Avaliação dos resultados.
6. Implantação e apresentação.

A evolução será controlada por atividades, com validação dos resultados antes do início da etapa seguinte.

## 10. Qualidade dos dados — diagnóstico inicial

A inspeção local identificou os seguintes pontos de atenção na fonte de vendas:

| Verificação | Resultado |
|---|---:|
| Registros de vendas | 10.012 |
| Valores ausentes em `vendedor_id` | 10 |
| Valores ausentes em `canal_venda` | 10 |
| Valores ausentes em `desconto` | 15 |
| Pares de registros integralmente duplicados | 12 |
| Linhas envolvidas nas duplicações | 24 |

As tabelas de produtos e vendedores não apresentaram valores ausentes nem linhas integralmente duplicadas nessa inspeção inicial.

Esses resultados ainda deverão ser reproduzidos no Databricks. Nenhum tratamento será considerado concluído até que as regras sejam definidas e os resultados validados.

## 11. Indicadores previstos

- Receita bruta e receita líquida, conforme regras de negócio definidas.
- Volume de vendas e quantidade de unidades.
- Desempenho por período, produto, categoria e canal.
- Desempenho por vendedor e região.
- Descontos aplicados.
- Margem estimada, considerando custo, desconto e status da venda.

A definição final de cada indicador será documentada antes da implementação. Pedidos cancelados e devolvidos exigirão tratamento explícito para evitar distorções.

## 12. Critérios de sucesso

- Fontes ingeridas e reconciliadas com os dados de origem.
- Regras de qualidade documentadas e validadas.
- Camadas Bronze, Silver e Gold implementadas conforme os recursos disponíveis.
- Relacionamentos e cálculos testados.
- Indicadores reproduzíveis por meio de SQL.
- Dashboard funcional e documentado.
- Código e documentação versionados no GitHub.
- Limitações e decisões analíticas registradas.

## 13. Limitações e premissas

- Os dados são fictícios e não representam resultados de uma empresa real.
- Os indicadores dependem da qualidade das fontes e das regras de negócio aprovadas.
- A margem será estimada, não representando necessariamente o lucro contábil.
- O Databricks Free possui limites de uso e funcionalidades; a arquitetura será ajustada ao que estiver disponível no workspace.
- O GitHub será a vitrine pública do projeto. O acesso direto ao workspace e aos dashboards dependerá das permissões disponíveis.
- Nenhuma etapa será considerada concluída sem evidências de execução e validação.