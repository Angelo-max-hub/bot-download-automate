from processamento_de_texto import verificacao_de_igualdade as vi
import os
import ipdb
cm = lambda: os.system(input("> "))
def to_download(a_baixar: list[str], baixado: list[str]) -> list[str]:
    """
    Retorna quais arquivos não foram baixados anteriormente.

    Filtra de uma lista de nomes de arquivos apenas aqueles que não estão atualmente no computador, de
    maneira a não serem baixados novamente.
    """
    arquivos_a_baixar = []
    # Os nomes dos downloads salvos são muito diferentes dos arquivos originais disponiveis no SUAP, então 
    # verifico se o primeiro ou último nome dos arquivos originais está em algum item de 
    # "files_baixados", porque geralmente os nomes antigos se mantém em algum lugar do novo (veja
    # "_foi_baixado" função).
    arquivos_a_baixar = _filtrar_downloads_nao_feitos(a_baixar, baixado)

    return arquivos_a_baixar


def _filtrar_downloads_nao_feitos(downloads: list[str], files: list[str]) -> list[str]:
    ipdb.set_trace()
    arquivos_a_baixar = []
    par_encontrado = False
    for download in downloads:
        for file in files:
            if vi.verificar_igualdade1(download, file):
                arquivos_a_baixar.append(download)
                files.remove(file)
                par_encontrado = True
                break

        if not par_encontrado:
           correspondente = _verificacao_avancada_correspondencia(download, files) # "" or "string"
           if correspondente:
               arquivos_a_baixar.append(correspondente)

    return arquivos_a_baixar

def _verificacao_avancada_correspondencia(download: str, files: list[str]) -> str:
    for file in files:
        if vi.verificar_igualdade2(download, file):
            return file
        
    return False
def _all_the_files() -> list[str]:
    """
    Retorna uma lista com todos os arquivos (relevantes) já baixados no computador.

    Parameters:
    Nothing
    Returns:
    Uma lista contendo os nomes de documentos salvos no computador.
    """
    # Todos os documentos que são baixados no SUAP estão no Desktop ou em uma subpasta dedicada.
    destinos_documento = {"desktop": r"/home/angelo/Área de trabalho",
                          "doc_desktop": r"/home/angelo/Área de trabalho/documentos",
                          "doc_pasta_pessoal": r"/home/angelo/Área de trabalho/documentos/documentos da escola",
                          "download_auto": r"/home/angelo/Área de trabalho/documentos/downloads_automates"}
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
    ipdb.set_trace()
    arquivos_a_baixar = to_download(["teoria da comunicação - roman jackobson",
                                        "linguagem falada e linguagem escrita"], _all_the_files())