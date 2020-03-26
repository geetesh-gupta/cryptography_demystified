from utils.string import *
from utils.conversion import *
from utils.pprint import *

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

S_BOXES = [
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,
    ], [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9,
    ], [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,
    ], [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,
    ], [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3,
    ], [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13,
    ], [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
    ], [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11,
    ]
]

P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

left_shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

OFFSET = 1
ROUNDS_NUM = 16
DATA_SIZE = 64
KEY_SIZE = 64


def transform(key):
    # Initial key permutation
    initial_permutation = pad(permute(key, PC1, OFFSET))
    pprint(2, "IP_Key", initial_permutation)

    mid_index = len(initial_permutation) // 2

    # Initialize shifted keys
    shifted_keys = [initial_permutation]

    # Create shifted keys for each round
    for i in range(1, ROUNDS_NUM + 1):
        # Shift required for the round
        shift = left_shift_table[i - 1]

        # Key for the round
        key = shifted_keys[i - 1]

        left_side = lcs(key[:mid_index], shift)
        right_side = lcs(key[mid_index:], shift)

        shifted_keys.append(left_side + right_side)
    pprint(2, "Shifted keys", shifted_keys)

    permuted_choices = []
    for i in range(1, ROUNDS_NUM + 1):
        permuted_choices.append(pad(permute(shifted_keys[i], PC2, OFFSET)))
    pprint(2, "Permuted Choices", permuted_choices)
    return permuted_choices


def sbox(data):
    converted = ""
    divider = 6
    for i in range(len(data) // divider):
        row = int(data[i * divider + 0] + data[i * divider + divider - 1], 2)
        col = int(data[i * divider + 1:i * divider + divider - 1], 2)
        sbox_val = S_BOXES[i][16 * row + col]
        converted += pad(convert_to_bin(sbox_val, 10), 4)
    return converted


def f(data, key):
    # Expansion D-box
    expanded_data = pad(permute(data, E, OFFSET))
    pprint(3, "Expanded R", expanded_data)

    # XOR RoundKey[i] and right_expanded
    xored_str = xorstr(expanded_data, key)
    pprint(3, "XORed R", xored_str)

    # S-Boxes
    sbox_result = sbox(xored_str)
    pprint(3, "SBox R", sbox_result)

    return pad(permute(sbox_result, P, OFFSET))


def sub_per(msg, key, proc):
    pprint(1, "M", msg)
    pprint(1, "Key", key)

    # Initial Permutation
    initial_permutation = pad(permute(msg, IP, OFFSET))
    pprint(2, "IP_MSG", initial_permutation)

    # Create permuted keys set
    permuted_choices = transform(key)

    mid_index = len(initial_permutation) // 2

    # Swap left and right side
    left_side, right_side = initial_permutation[:mid_index], initial_permutation[mid_index:]

    # Rounds
    for i in range(1, ROUNDS_NUM + 1):
        # Get key
        round_key = ""
        if proc == "encrypt":
            round_key = permuted_choices[i - 1]
        elif proc == "decrypt":
            round_key = permuted_choices[ROUNDS_NUM - i]

        # Swap and apply function
        left_side, right_side = right_side, xorstr(left_side, f(right_side, round_key))
        pprint(2, "Round", i, "L", left_side)
        pprint(2, "Round", i, "R", right_side)
        pprint(2)

    # Swap left and right to get semi final val
    semifinal_val = right_side + left_side

    # Final Permutation
    final_permutation = pad(permute(semifinal_val, IP_INV, OFFSET))
    pprint(1, "CipherText Binary", final_permutation)

    return final_permutation


def encrypt(msg, key):
    ciphertext = ""
    for i in range(len(msg) // DATA_SIZE):
        ciphertext += sub_per(msg[i * DATA_SIZE:(i + 1) * DATA_SIZE], key, "encrypt")
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext) // DATA_SIZE):
        plaintext += sub_per(ciphertext[i * DATA_SIZE:(i + 1) * DATA_SIZE], key, "decrypt")
    return plaintext
