def cifra_trilho_encriptar(texto, trilhos):

    texto_cifrado = ''

    for trilho in range(trilhos):
        i = trilho
        while i < len(texto):
            texto_cifrado += texto[i]
            if trilho == 0 or trilho == trilhos - 1:
                i += 2 * (trilhos - 1)
            else:
                i += 2 * (trilhos - trilho - 1)
                if i < len(texto):
                    texto_cifrado += texto[i]
                    i += 2 * trilho
    return texto_cifrado


def cifra_trilho_desencriptar(texto_cifrado, trilhos):

    texto = [''] * len(texto_cifrado)

    k = 0
    for trilho in range(trilhos):
        i = trilho
        while i < len(texto_cifrado):
            texto[i] = texto_cifrado[k]
            k += 1
            if trilho == 0 or trilho == trilhos - 1:
                i += 2 * (trilhos - 1)
            else:
                i += 2 * (trilhos - trilho - 1)
                if i < len(texto_cifrado):
                    texto[i] = texto_cifrado[k]
                    k += 1
                    i += 2 * trilho
    return ''.join(texto)


texto_original = "Francisco Remo Silva Souza Filho"
texto_cifrado_trilho = cifra_trilho_encriptar(texto_original, 5)
texto_descriptografado_trilho = cifra_trilho_desencriptar(texto_cifrado_trilho, 5)

print("Texto Criptografado:", texto_cifrado_trilho)
print("Texto Descriptografado:", texto_descriptografado_trilho)

