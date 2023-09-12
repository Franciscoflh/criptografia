def cifra_coluna_encriptar(texto, chave):

    num_cols = len(chave)
    num_rows = -(-len(texto) // num_cols)
    num_padding = num_rows * num_cols - len(texto)
    texto += 'X' * num_padding

    retangulo = [texto[i:i+num_cols] for i in range(0, len(texto), num_cols)]

    texto_cifrado = ''
    for col_num in sorted([(char, i) for i, char in enumerate(chave)], key=lambda x: x[0]):
        col_idx = col_num[1]
        for row in retangulo:
            texto_cifrado += row[col_idx]

    return texto_cifrado


def cifra_coluna_desencriptar(texto_cifrado, chave):

    num_cols = len(chave)
    num_rows = len(texto_cifrado) // num_cols

    retangulo = [[''] * num_cols for _ in range(num_rows)]
    k = 0
    for col_num in sorted([(char, i) for i, char in enumerate(chave)], key=lambda x: x[0]):
        col_idx = col_num[1]
        for row in range(num_rows):
            retangulo[row][col_idx] = texto_cifrado[k]
            k += 1

    texto = ''.join([''.join(row) for row in retangulo])

    return texto.rstrip('X')


texto_original = "Francisco Remo Silva Souza Filho"
texto_cifrado_coluna = cifra_coluna_encriptar(texto_original, "ZEBRA")
texto_descriptografado_coluna = cifra_coluna_desencriptar(texto_cifrado_coluna, "ZEBRA")
print("Texto Criptografado:", texto_cifrado_coluna)
print("Texto Descriptografado:", texto_descriptografado_coluna)
