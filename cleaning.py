
def limpar_dados(df):
    df = df.copy()
    
    df["nome"] = df["nome"].str.strip().str.title()
    df["email"] = df["email"].str.strip().str.lower()
    df["cidade"] = df["cidade"].str.strip().str.title()
    
    return df