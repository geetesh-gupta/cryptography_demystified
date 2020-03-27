def convert_to_bin(inp, scale):
    if isinstance(inp, str):
        inp = str_to_int(inp, scale)
    bin_str = bin(inp)
    bin_wo0b = bin_str[2:]
    return bin_wo0b


def convert_to_hex(inp, scale):
    if isinstance(inp, str):
        inp = str_to_int(inp, scale)
    hex_str = hex(inp)
    hex_wo0x = hex_str[2:]
    return hex_wo0x


def convert_to_dec(inp, scale):
    if isinstance(inp, str):
        return str_to_int(inp, scale)
    return inp


def str_to_int(string, scale):
    return int(string, scale)


def hexbin(hex_str):
    return convert_to_bin(hex_str, 16)


def binhex(bin_str):
    return convert_to_hex(bin_str, 2)


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


def rcs(string, shift):
    return lcs(string, len(string) - shift)


def xorstr(str1, str2):
    xored_str = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            xored_str += "0"
        else:
            xored_str += "1"
    return xored_str


def hexstr2hexlist(hexstr, offset):
    lis = []
    for i in range(0, len(hexstr), offset):
        lis.append(int(hexstr[i:i + offset], 16))
    return lis


def hexlist2hexstr(hexlist, offset):
    string = ""
    for i in range(len(hexlist)):
        for j in range(len(hexlist[i])):
            string += pad(convert_to_hex(hexlist[i][j], 10), 2)
    return string


def xor_bytes(a, b):
    """ Returns a new byte array with the elements xor'ed. """
    return bytes(i ^ j for i, j in zip(a, b))


def bytes2matrix(bytes):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(bytes[i:i + 4]) for i in range(0, len(bytes), 4)]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))


def inc_bytes(a):
    """ Returns a new byte array with the value increment by 1 """
    out = list(a)
    for i in reversed(range(len(out))):
        if out[i] == 0xFF:
            out[i] = 0
        else:
            out[i] += 1
            break
    return bytes(out)
