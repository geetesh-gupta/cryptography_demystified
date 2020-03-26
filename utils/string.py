def permute(old_bits, offset_table, offset):
    new_bits = ""
    for i in range(len(offset_table)):
        new_bits += old_bits[offset_table[i] - offset]
    return new_bits


def pad(string, padding=8):
    to_pad = len(string) % padding
    str_padded = string[to_pad:]
    if to_pad:
        str_padded = string[:to_pad].zfill(padding) + str_padded
    return str_padded


def lcs(string, shift):
    return string[shift:] + string[:shift]


def xorstr(str1, str2):
    xored_str = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            xored_str += "0"
        else:
            xored_str += "1"
    return xored_str