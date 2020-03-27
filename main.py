import sys
import des
import aes
from utils.pprint import pprint


def main():
    if sys.argv[1] == "des":
        msg = "0000000100100011010001010110011110001001101010111100110111101111"
        key = "0001001100110100010101110111100110011011101111001101111111110001"
        pprint(0, "Msg", msg)
        pprint(0, "Key", key)

        ciphertext = des.encrypt(msg, key)
        pprint(0, "Cipher", ciphertext)

        plaintext = des.decrypt(ciphertext, key)
        pprint(0, "PlainText", plaintext)

        if plaintext == msg:
            pprint(0, "Plaintext is equal to Msg")
    elif sys.argv[1] == "aes":
        msg = "0123456789abcdeffedcba9876543210"
        key = "0f1571c947d9e8590cb7add6af7f6798"
        pprint(0, "Msg", msg)
        pprint(0, "Key", key)

        ciphertext = aes.encrypt(msg, key)
        pprint(0, "Cipher", ciphertext)

        plaintext = aes.decrypt(ciphertext, key)
        pprint(0, "PlainText", plaintext)

        if plaintext == msg:
            pprint(0, "Plaintext is equal to Msg")
if __name__ == "__main__":
    main()
