import os
import ipdb

def to_download(a_baixar: list[str]) -> list[str]:
    """
    Retorna quais arquivos não foram baixados anteriormente.

    Filtra de uma lista de nomes de arquivos apenas aqueles que não estão atualmente no computador, de
    maneira a não serem baixados novamente.
    """
    arquivos_a_baixar = []
    # Os nomes dos downloads salvos são muito diferentes dos arquivos originais disponiveis no SUAP, então 
    # verifico se o primeiro e último nome dos arquivos originais está em algum item de 
    # "files_baixados", porque geralmente os nomes antigos se mantém em algum lugar do novo (veja
    # "_foi_baixado" função).
    files_ja_baixados = _all_the_files()
    for file in a_baixar:
        if not _foi_baixado(file, files_ja_baixados):
            arquivos_a_baixar.append(file)

    return arquivos_a_baixar


def _foi_baixado(file: str, downloads) -> bool:
    file_split = file.split(" ")
    for download in downloads:
        if file_split[0] in download and file_split[-1] in download:
            return True
def _all_the_files() -> list[str]:
    """
    Retorna uma lista com todos os arquivos (relevantes) já baixados no computador.

    Parameters:
        Nothing
    Returns:
        Uma lista contendo os nomes de documentos salvos no computador.
    """
    # Todos os documentos que são baixados no SUAP estão no Desktop ou em uma subpasta dele.
    destinos_documento = {"desktop": "/home/angelo/Área de trabalho",
                          "doc_desktop": "/home/angelo/Área de trabalho/documentos",
                          "doc_pasta_pessoal": "/home/angelo/Área de trabalho/documentos/documentos da escola"}
    arquivos_existentes = []

    for diretorio in destinos_documento.values():
        conteudo = os.listdir(diretorio)
        arquivos_filtrados = filter(_tipo_certo, conteudo)
        arquivos_existentes.extend(list(arquivos_filtrados))
        
    return arquivos_existentes
def _tipo_certo(arquivo: str) -> bool:
    tipos_validos = [".pdf", ".docx"]
    nome, extencao = os.path.splitext(arquivo)

    return extencao in tipos_validos

if __name__ == "__main__":
   print(to_download(["Gêneros textuais", "Coisa aleatoria"]))