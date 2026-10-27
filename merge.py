import pandas as pd
from cleaning import limpar_dados
from duplicates import remover_duplicatas
from pathlib import Path

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

df_final, quantidade = remover_duplicatas(df_limpo)

# Relatorio
print("\n === RELATORIO FINAL ===")
print(f"\Arquivos processados: {len(arquivos)}")
print(f"\nRegistros unificados: {df_unificado.shape[0]}")
print(f"\nDuplicatas removidas: {quantidade}")
print(f"\nRegistros finais: {df_final.shape[0]}")

# mostrar resultado
print("\n === DADOS UNIFICADOS ===")
print(df_final)

# testes de integracao
assert df_unificado.shape[0] == sum(
    df.shape[0] for df in dataframes
)

assert df_final.shape[0] == df_unificado.shape[0] - quantidade

assert not df_final.duplicated().any()

assert (
    df_final["email"]
    == df_final["email"].str.strip().str.lower()
).all()

print("\nTestes de integracao passaram!")

# EXPORTACAO DOS DADOS
pasta_saida = Path("output")
pasta_saida.mkdir(exist_ok=True)

arquivo_saida = pasta_saida / "clientes_tratados.csv"

with arquivo_saida.open("x", encoding="utf-8-sig", newline="") as arquivo:
    df_final.to_csv(arquivo, index=False)

print(f"Arquivo salvo em: {arquivo_saida}")