def clean_inp(inp):
    return inp.upper().replace(" ", "")  # Convert to upper case, remove whitespace


def encrypt(message, key):
    m = clean_inp(message)
    k = clean_inp(key)
    ciphertext = ""
    for i in range(len(m)):
        letter = (ord(m[i]) - 65 + ord(k[i]) - 65) % 26 + 65
        ciphertext += chr(letter)
    return ciphertext


def decrypt(message, key):
    m = clean_inp(message)
    k = clean_inp(key)
    plaintext = ""
    for i in range(len(m)):
        letter = (ord(m[i]) - ord(k[i])) % 26 + 65
        plaintext += chr(letter)
    return plaintext
