import time
def verificar_igualdade1(name_download: str, name_file: str) -> bool:
    name_download = name_download.split(" ")

    return name_download[0] in name_file and name_download[-1] in name_file

def verificar_igualdade2(name_download: str, file: str) -> bool:
    palavras_frase = name_download.split(" ")
    words = (palavras_frase[0], palavras_frase[-1])
    partes = []
    for word in words:
        max_time, max_len = _max_time_len(word)
        partes.extend(
            _word_split(word, max_time, max_len)
            )
                
    return _it_is_in_file(partes, file)
def _max_time_len(word):
    len_word = len(word)

    if len_word <= 5:
        tamanho_parte = len_word // 2
        max_time = 2
    else:
        tamanho_parte = len_word // 3
        max_time = 3

    return tamanho_parte, max_time
def _word_split(word, max_time, max_len):
    partes = []
    time = 1
    i = 0
    j = i + max_len
    while time <= max_time:
        if time < max_time:
            partes.append(word[i:j])

            time += 1
            i += max_len
            j += max_len
        else:
            partes.append(word[i:])
            time += 1
    return partes

def _it_is_in_file(partes_word, file):
    word1_ok = \
        partes_word[0] in file or \
        partes_word[1] in file or \
        partes_word[2] in file
    word2_ok = \
        partes_word[0] in file or \
        partes_word[1] in file or \
        partes_word[2] in file
    
    return word1_ok and word2_ok
if __name__ == "__main__":
    print(verificar_igualdade2("Linguagem falada e escrita", "Estou no mundo da lua"))
    