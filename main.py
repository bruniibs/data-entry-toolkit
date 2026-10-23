import pandas as pd

df = pd.read_csv("data/clients.csv")

print("=== Dados Originais ===")
print(df)

# padronizar nomes
df['nome'] = df["nome"].str.strip().str.title()

# padronizar emails
df["email"] = df["email"].str.strip().str.lower()

# padronizar cidades
df["cidade"] = df["cidade"].str.strip().str.title()


# remoção de duplicatas
total_antes = df.shape[0]

duplicates = df.duplicated().sum()
df = df.drop_duplicates()

total_depois = df.shape[0]

# relatorio
print("\n=== RELATORIO DE LIMPEZA ===")
print(f"Registros antes: {total_antes}")
print(f"Duplicatas removidas: {duplicates}")
print(f"Registros depois: {total_depois}")

print("\n=== DADOS LIMPOS ===")
print(df)