import pandas as pd
from pathlib import Path

def exportar_csv(df, pasta="output"):
    pasta_saida = Path(pasta)
    pasta_saida.mkdir(parents=True, exist_ok=True)
    
    contador = 0
    
    while True:
        if contador == 0:
            nome = "clientes_tratados.csv"
        else:
            nome = f"clientes_tratados_{contador:03d}.csv"
        
        caminho = pasta_saida / nome
        
        try:
            with caminho.open("x", encoding="utf-8-sig", newline="") as arquivo:
                df.to_csv(arquivo, index=False)
            
            # ler arquivo que acabamos de salvar
            df_verificacao = pd.read_csv(
                caminho,
                encoding="utf-8-sig"
            )
            
            # comparar os dados
            pd.testing.assert_frame_equal(
                df.reset_index(drop=True),
                df_verificacao,
                check_dtype=False
            )
            
            print("Validação do csv concluida!")
            
            return caminho
        
        except FileExistsError:
            contador += 1
            continue