import pandas as pd

from cleaning import normalizar_ausentes, relatorio_ausentes


def test_normaliza_valores_ausentes():
    df = pd.DataFrame({
        "nome": ["Ana", "Bruno", "Carla", "Diego"],
        "email": [
            "ana@example.com",
            "",
            None,
            "   ",
        ]
    })

    resultado = normalizar_ausentes(df)

    assert resultado["email"].isna().sum() == 3
    assert resultado.loc[0, "email"] == "ana@example.com"
    assert len(resultado) == 4


def test_relatorio_valores_ausentes():
    df = pd.DataFrame({
        "nome": ["Ana", "Bruno", "Carla"],
        "email": ["ana@example.com", pd.NA, pd.NA],
        "cidade": ["São Paulo", "Arujá", pd.NA]
    })

    resultado = relatorio_ausentes(df)

    assert resultado["nome"] == 0
    assert resultado["email"] == 2
    assert resultado["cidade"] == 1
