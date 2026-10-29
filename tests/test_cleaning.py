import unittest
import pandas as pd

from cleaning import limpar_dados


class TestLimparDados(unittest.TestCase):
    def test_padroniza_campos(self):
        entrada = pd.DataFrame({
                "nome": ["  ana silva  "]
                "email": [" ANA@EXAMPLE.COM"]
                "cidade": ["  sao paulo  "]
        })
        
        resultado = limpar_dados(entrada)
        
        self.assertEqual(resultado.loc[0, "nome"], "Ana Silva")
        self.assertEqual(resultado.loc[0, "email"], "ana@example.com")
        self.assertEqual(resultado.loc[0, "cidade"], "Sao Paulo")