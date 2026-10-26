import pandas as pd
from cleaning import limpar_dados

# ler os dois arquivos csv
arquivos = [
    "data/clients_01.csv",
    "data/clients_02.csv"
]

# lista de dfs, comeca vazia e a medida que for lendo vai adicionar df a ela
dataframes = []

for arquivo in arquivos:
    df = pd.read_csv(arquivo)
    dataframes.append(df)

# Unificar os DataFrames
df_unificado = pd.concat(dataframes, ignore_index=True)
df_limpo = limpar_dados(df_unificado)

# Relatorio
print("\n === RELATORIO DE UNIFICACAO ===")
print(f"\nTotal de arquivos: {len(arquivos)}")
print(f"\nTotal de registros unificados: {df_unificado.shape[0]}")

# mostrar resultado
print("\n === DADOS UNIFICADOS ===")
print(df_unificado)