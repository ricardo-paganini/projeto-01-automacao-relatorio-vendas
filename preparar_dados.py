import pandas as pd
from pathlib import Path

arquivo_excel = Path('dados_projeto_01.xlsx')
pasta_dados = Path('dados')

pasta_dados.mkdir(exist_ok=True)

dados_vendas = pd.read_excel(arquivo_excel, sheet_name='vendas')
dados_produtos = pd.read_excel(arquivo_excel, sheet_name='produtos')
dados_vendedores = pd.read_excel(arquivo_excel, sheet_name='vendedores')

dados_vendas.to_csv(pasta_dados / 'vendas.csv', index=False, encoding='utf-8-sig')

dados_produtos.to_csv(pasta_dados / 'produtos.csv', index=False, encoding='utf-8-sig')

dados_vendedores.to_csv(pasta_dados / 'vendedores.csv', index=False, encoding='utf-8-sig')

print('Arquivos CSV criados com sucesso!')