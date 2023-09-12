def cifra_vigenere_encriptar(texto, chave):

    texto_cifrado = ''

    for i, char in enumerate(texto):
        if char.isalpha():
            shift = ord(chave[i % len(chave)].upper()) - ord('A')
            if char.isupper():
                texto_cifrado += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                texto_cifrado += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            texto_cifrado += char

    return texto_cifrado


def cifra_vigenere_desencriptar(texto_cifrado, chave):

    texto = ''

    for i, char in enumerate(texto_cifrado):
        if char.isalpha():
            shift = ord(chave[i % len(chave)].upper()) - ord('A')
            if char.isupper():
                texto += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                texto += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            texto += char

    return texto


texto_original = "Francisco Remo Silva Souza Filho"
chave_vigenere = "KEY"
texto_cifrado_vigenere = cifra_vigenere_encriptar(texto_original, chave_vigenere)
texto_descriptografado_vigenere = cifra_vigenere_desencriptar(texto_cifrado_vigenere, chave_vigenere)

print("Texto Criptografado:", texto_cifrado_vigenere)
print("Texto Descriptografado:", texto_descriptografado_vigenere)
