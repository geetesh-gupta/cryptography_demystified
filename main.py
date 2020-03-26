import sys
from des import encrypt, decrypt
from utils.pprint import pprint


def main():
    if sys.argv[1] == "des":
        msg = "0000000100100011010001010110011110001001101010111100110111101111"
        key = "0001001100110100010101110111100110011011101111001101111111110001"
        pprint(0, "Msg", msg)
        pprint(0, "Key", key)

        ciphertext = encrypt(msg, key)
        pprint(0, "Cipher", ciphertext)

        plaintext = decrypt(ciphertext, key)
        pprint(0, "PlainText", plaintext)

        if plaintext == msg:
            pprint(0, "Plaintext is equal to Msg")


if __name__ == "__main__":
    main()
