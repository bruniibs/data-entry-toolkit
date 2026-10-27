
def limpar_dados(df):
    df = df.copy()
    
    colunas_obrigatorias = {"nome", "email", "cidade"}
    
    colunas_faltantes = (
        colunas_obrigatorias - set(df.columns)
    )
    
    if colunas_faltantes:
        raise ValueError(
            f"Colunas ausentes: {sorted(colunas_faltantes)}"
        )
    
    df["nome"] = df["nome"].str.strip().str.title()
    df["email"] = df["email"].str.strip().str.lower()
    df["cidade"] = df["cidade"].str.strip().str.title()
    
    return df
