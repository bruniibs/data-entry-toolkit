import pandas as pd
from cleaning import (
    limpar_dados,
    normalizar_ausentes,
    relatorio_ausentes
)
from duplicates import remover_duplicatas
from pathlib import Path
from export import exportar_csv

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

# limpar dupes
df_limpo = limpar_dados(df_unificado)

# Normalizar valores vazios
df_normalizado = normalizar_ausentes(df_limpo)

# Gerar relatorio antes de remover duplicatas
relatorio = relatorio_ausentes(df_normalizado)

# Remover duplicatas
df_final, quantidade = remover_duplicatas(df_normalizado)

# Relatorio
print("\n === RELATORIO FINAL ===")
print(f"\nArquivos processados: {len(arquivos)}")
print(f"\nRegistros unificados: {df_unificado.shape[0]}")
print(f"\nDuplicatas removidas: {quantidade}")
print(f"\nRegistros finais: {df_final.shape[0]}")

# mostrar resultado
print("\n === DADOS UNIFICADOS ===")
print(df_final)

print("\n=== RELATÓRIO DE VALORES AUSENTES ===")

for coluna, quantidade_ausente in relatorio.items():
    print(f"{coluna}: {quantidade_ausente}")

# testes de integracao
assert df_unificado.shape[0] == sum(
    df.shape[0] for df in dataframes
)

assert df_final.shape[0] == df_unificado.shape[0] - quantidade

assert not df_final.duplicated().any()

emails_validos = df_final["email"].dropna()

assert (
    emails_validos
    == emails_validos.str.strip().str.lower()
).all()

print("\nTestes de integracao passaram!")

# EXPORTACAO DOS DADOS
caminho = exportar_csv(df_final)

print(f"\nArquivo criado: {caminho}")
