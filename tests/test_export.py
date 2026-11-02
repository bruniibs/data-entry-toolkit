import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd

from export import exportar_csv


class TestExportarCsv(unittest.TestCase):
    def test_exporta_csv_com_dados_corretos(self):
        entrada = pd.DataFrame({
            "nome": ["Ana Silva"],
            "email": ["ana@example.com"],
            "cidade": ["Sao Paulo"],
        })
        
        with TemporaryDirectory() as pasta:
            caminho = exportar_csv(entrada, pasta=pasta)
            
            self.assertTrue(caminho.is_file())
            self.assertEqual(
                caminho,
                Path(pasta) / "clientes_tratados.csv",
            )
            
            resultado = pd.read_csv(
                caminho,
                encoding="utf-8-sig",
            )
            
            pd.testing.assert_frame_equal(resultado, entrada)
    
    def test_preserva_arquivo_existente(self):
        primeiro = pd.DataFrame({
            "nome": ["Ana Silva"],
            "email": ["ana@example.com"],
            "cidade": ["Sao Paulo"],
        })
        
        segundo = pd.DataFrame({
            "nome": ["Maria Costa"],
            "email": ["maria@example.com"],
            "cidade": ["Curitiba"],
        })
        
        with TemporaryDirectory() as pasta:
            caminho_1 = exportar_csv(primeiro, pasta=pasta)
            conteudo_original = caminho_1.read_bytes()
            
            caminho_2 = exportar_csv(segundo, pasta=pasta)
            
            self.assertEqual(
                caminho_2.name,
                "clientes_tratados_001.csv",
            )
            self.assertTrue(caminho_2.is_file())
            
            self.assertEqual(
                caminho_1.read_bytes(),
                conteudo_original,
            )
            
            resultado_2 = pd.read_csv(
                caminho_2,
                encoding="utf-8-sig",
            )
            
            pd.testing.assert_frame_equal(resultado_2, segundo)