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

print("\n=== DADOS LIMPOS ===")
print(df)