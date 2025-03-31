import os

# Criar uma lista para adicionar os nomes dos arquivos
# Para cada diretório-destino, capturar todos os arquivos existentes, os diferenciando de pastas.


def all_the_files() -> list[str]:
    """
    Retorna uma lista com todos os arquivos (relevantes) já baixados no computador.

    Parameters:
        Nothing
    Returns:
        None
    """
    # Todos os documentos que são baixados no SUAP estão no Desktop ou em uma subpasta dele.
    destinos_documento = {"desktop": "/home/angelo/Área de trabalho",
                          "doc_desktop": "/home/angelo/Área de trabalho/documentos",
                          "doc_pasta_pessoal": "/home/angelo/Área de trabalho/angelo/documentos da escola"}
    arquivos_existentes = []

    for diretorio in destinos_documento:
        caminho = destinos_documento[diretorio]
        conteudo = os.listdir(caminho)
        arquivos_filtrados = filter(_tipo_certo, conteudo)
        arquivos_existentes.extend(list(arquivos_filtrados))
        
    return arquivos_existentes

def _tipo_certo(arquivo: str) -> bool:
    tipos_validos = [".txt", ".pdf", ".docx"]
    nome, extencao = os.path.splitext(arquivo)
    return extencao in tipos_validos

if __name__ == "__main__":
    pass