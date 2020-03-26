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
