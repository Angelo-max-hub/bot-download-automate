import unicodedata as un

# Esta função retorna uma string processada que deve ser usada como parâmetro de "to_download", que 
# retorna quais links devem ser clicados com base no nome do link. 
# Isso é necessário porque "to_download" usa o algorítimo de similaridade de string "Jaro Similarity". 
# A biblioteca Unicodedata é usada para tirar caracteres especiais.

def processar(string: str, name_file= ""):
    # Deixar tudo minúsculo.
    str_processada  = string.lower()

    # Tirar acentuação.
    str_processada = un.normalize("NFD", str_processada).encode("ascii", "ignore").decode("ascii")

    # Tirar espaços.
    str_processada = str_processada.replace(" ", "")

    if name_file:
        _processar_strings(str_processada, name_file)

def _processar_strings(str_processada: str, name_file: str):
    # Deixar minúsculo, tirar espaços, tirar underlines e tirar underscore.
    name_file = name_file.lower().replace("_", "").replace("-", "")
    componentes_name = name_file.

if __name__  == "__main__":
    processar("ÂNGÉLÕ LOPES RODRIGUES", "LOPÉS")