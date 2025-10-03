from pathlib import Path

def ler_arquivo(caminho_arquivo):
     caminho_arquivo = Path(caminho_arquivo)
     return caminho_arquivo.read_text(encoding="utf-8")
def escrever_arquivo(caminho_arquivo, links):
    caminho_arquivo = Path(caminho_arquivo)
    modo = 'a' if caminho_arquivo.is_file() else 'w'

    with caminho_arquivo.open(modo, encoding="utf-8") as file:
        file.write("\n".join(links))