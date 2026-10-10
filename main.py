import pandas as pd

df = pd.read_csv("data/clients.csv")

# exibir primeiras linhas
print("=== Primeiras linhas ===")
print(df.head())

# Exibir quantidade de registros
print("\n=== Total de registros ===")
print(f"Total de registros: {df.shape[0]}")

# Exibir nomes dass colunas
print("\n=== Colunas ===")
print(f"Total de colunas: {df.shape[1]}")