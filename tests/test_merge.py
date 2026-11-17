import subprocess
import sys
import pandas as pd
from pathlib import Path
from shutil import copyfile


def test_merge_com_csvs_ficticios(tmp_path):
    pasta_dados = tmp_path / "data"
    pasta_dados.mkdir()
    pasta_fixtures = Path(__file__).parent / "fixtures"

    origem = pasta_fixtures / "clients_01.csv"
    destino = pasta_dados / "clients_01.csv"
    copyfile(origem, destino)
    assert destino.is_file()

    origem = pasta_fixtures / "clients_02.csv"
    destino = pasta_dados / "clients_02.csv"
    copyfile(origem, destino)
    assert destino.is_file()

    raiz_projeto = Path(__file__).resolve().parent.parent
    script_merge = raiz_projeto / "merge.py"
    execucao = subprocess.run(
        [sys.executable, str(script_merge)],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    )

    csv_exportado = tmp_path / "output" / "clientes_tratados.csv"
    assert csv_exportado.is_file()

    resultado = pd.read_csv(csv_exportado, encoding="utf-8-sig")
    assert len(resultado) == 3

    nomes = resultado["nome"].tolist()
    assert nomes == [
        "Ana Silva",
        "Bruno Costa",
        "Carla Souza",
    ]

    email_bruno = resultado.loc[1, "email"]
    assert pd.isna(email_bruno)
    
    cidade_carla = resultado.loc[2, "cidade"]
    assert pd.isna(cidade_carla)

    linhas_relatorio = execucao.stdout.splitlines()
    assert "email: 1" in linhas_relatorio
    assert "cidade: 1" in linhas_relatorio
