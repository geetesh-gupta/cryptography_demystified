import sys
import des
import aes
import vernam
import caesar
from utils.pprint import pprint


def run(msg, key, algo):
    pprint(0, "Msg", msg)
    pprint(0, "Key", key)

    ciphertext = algo.encrypt(msg, key)
    pprint(0, "Cipher", ciphertext)

    plaintext = algo.decrypt(ciphertext, key)
    pprint(0, "PlainText", plaintext)

    if plaintext == msg:
        pprint(0, "Plaintext is equal to Msg")


def main():
    if sys.argv[1] == "des":
        run("0000000100100011010001010110011110001001101010111100110111101111",
            "0001001100110100010101110111100110011011101111001101111111110001",
            des)
    elif sys.argv[1] == "aes":
        run("0123456789abcdeffedcba9876543210",
            "0f1571c947d9e8590cb7add6af7f6798",
            aes)
    elif sys.argv[1] == "vernam":
        run("RAMSWARUPK",
            "RANCHOBABA",
            vernam)

    elif sys.argv[1] == "caesar":
        run("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            23,
            caesar)


if __name__ == "__main__":
    main()
