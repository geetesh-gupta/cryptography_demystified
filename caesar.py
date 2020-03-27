def shift_by_n(msg, n):
    shifted_msg = ""

    for c in msg:
        base = 65
        if c.islower():
            base = 97
        shifted_msg += chr((ord(c) + n - base) % 26 + base)
    return shifted_msg


def encrypt(msg, shift):
    return shift_by_n(msg, shift)


def decrypt(msg, shift):
    return shift_by_n(msg, -shift)
