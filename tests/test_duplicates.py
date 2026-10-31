import unittest
import pandas as pd

from duplicates import remover_duplicatas


class TestRemoverDuplicatas(unittest.TestCase):
    def test_remove_duplicatas_e_informa_quantidade(self):
        entrada = pd.DataFrame({
            "nome": ["Ana Silva", "Ana Silva", "Maria Costa"],
            "email": [
                "ana@example.com",
                "ana@example.com",
                "maria@example.com",
            ],
            "cidade": ["Sao Paulo", "Sao Paulo", "Curitiba"],
        })
        
        resultado, quantidade = remover_duplicatas(entrada)
        
        esperado = pd.DataFrame({
            "nome": ["Ana Silva", "Maria Costa"],
            "email": ["ana@example.com", "maria@example.com"],
            "cidade": ["Sao Paulo", "Curitiba"],
        })
        
        self.assertEqual(quantidade, 1)
        
        pd.testing.assert_frame_equal(
            resultado.reset_index(drop=True),
            esperado,
        )
    
    def test_preserva_dados_sem_duplicatas(self):
        entrada = pd.DataFrame({
            "nome": ["Ana Silva", "Maria Costa"],
            "email": ["ana@example.com", "maria@example.com"],
            "cidade": ["Sao Paulo", "Curitiba"],
        })
        
        resultado, quantidade = remover_duplicatas(entrada)
        
        self.assertEqual(quantidade, 0)
        pd.testing.assert_frame_equal(resultado, entrada)