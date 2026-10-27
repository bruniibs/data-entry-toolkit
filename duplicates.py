
def remover_duplicatas(df):
    # criar copia dos dados
    df = df.copy()
    
    # contar duplicatas
    quantidade = df.duplicated().sum()
    
    # remover dups
    df = df.drop_duplicates()
    
    # devolver dados e quantidade removida
    return df, quantidade