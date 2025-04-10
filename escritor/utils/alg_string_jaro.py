import ipdb

# Algorítimo de Jaro Similarity. Usarei ele para determinar quando os arquivos no SUAP estão salvos no 
# computador, porque os nomes dos links para dowload são sempre diferentes dos arquivos salvos.

def jaro_similarity(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    limite = max(len_str1, len_str2) // 2 - 1

    # Caracteres com correspondentes do segundo texto (len_str2).
    corresp2 = [-1] * len_str2

    # Contar as correspondências.

    correspondecias = 0
    for i in range(len_str1):
        start = max(0, i - limite)
        end = min(i + limite + 1, len_str2)
        for j in range(start, end):
            if str1[i] == str2[j] and corresp2[j] == -1:
                correspondecias += 1
                corresp2[j] = i
                break
    if correspondecias == 0:
        return 0.0
    
    # Contar transposições.
    indices_errados = 0
    for k in range(len_str2):
        if corresp2[k] != -1:
            if k != corresp2[k]:
                indices_errados += 1
    
    transposicoes = indices_errados / 2

    # Formula matemática de Jaro.
    c_por_s1 = correspondecias / len_str1
    c_por_s2 = correspondecias / len_str2
    c_menos_t_por_c = (correspondecias - transposicoes) / correspondecias
    similaridade = (1/3) * (c_por_s1 + c_por_s2 + c_menos_t_por_c)

    return round(similaridade, 2)
if __name__ == "__main__":
    print(jaro_similarity("linguagemfaladaeescrita", "linguagemfaladaelinguagemescrita"))