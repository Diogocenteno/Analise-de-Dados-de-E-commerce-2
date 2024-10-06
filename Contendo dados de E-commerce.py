import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Inspecionar os valores da coluna 'Desconto' para identificar inconsistências
print("Valores únicos na coluna 'Desconto' antes da extração:")
print(df['Desconto'].unique())

# Converta a coluna Desconto para o tipo string e extraia apenas o valor numérico
df['Desconto'] = df['Desconto'].astype(str).str.extract(r'(\d+)%?')[0]

# Verificar a consistência do tipo após a extração
df['Desconto'] = df['Desconto'].astype(str)

# Verificar se ainda existem NaNs
if df['Desconto'].isnull().any():
    print("Ainda existem NaNs na coluna 'Desconto':")
    print(df[df['Desconto'].isnull()])

# Criar novas colunas baseadas na coluna Condicao
split_condicao = df['Condicao'].str.split(' \| ', n=1, expand=True)
df['Condicao_Atual'] = split_condicao[0].str.strip()

# Verificar se a segunda parte existe antes de acessar
df['Qtd_Vendidos'] = split_condicao[1].str.strip() if split_condicao.shape[1] > 1 else None

# Inspecionar os valores da coluna 'Qtd_Vendidos' antes da extração
print("Valores únicos na coluna 'Qtd_Vendidos' antes da extração:")
print(df['Qtd_Vendidos'].unique())

# Ajustar a extração da quantidade de itens vendidos
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].str.extract(r'(\+\d+mil|\+\d+|\d+mil|\d+)')[0]

# Preencher NaNs na coluna 'Qtd_Vendidos' com 'Nenhum'
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].fillna('Nenhum')

# Exibir as primeiras linhas do DataFrame atualizado
print(df.head())