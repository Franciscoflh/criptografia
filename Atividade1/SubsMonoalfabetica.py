import string


def cifra_mono_encriptar(texto, chave):

    mapeamento = str.maketrans(string.ascii_uppercase, chave)

    return texto.translate(mapeamento)


def cifra_mono_desencriptar(texto_cifrado, chave):

    mapeamento = str.maketrans(chave, string.ascii_uppercase)

    return texto_cifrado.translate(mapeamento)


texto_original = "Francisco Remo Silva Souza Filho"
chave_mono = "QWERTYUIOPASDFGHJKLZXCVBNM"
texto_cifrado_mono = cifra_mono_encriptar(texto_original, chave_mono)
texto_descriptografado_mono = cifra_mono_desencriptar(texto_cifrado_mono, chave_mono)

print("Texto Criptografado:", texto_cifrado_mono)
print("Texto Descriptografado:", texto_descriptografado_mono)
