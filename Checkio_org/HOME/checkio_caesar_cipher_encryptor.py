import string


def to_encrypt(text: str, delta: int) -> str:
    letters_str = string.ascii_lowercase
    len_letters_str = len(letters_str)
    result_string = ""
    for symbol in text:
        if symbol == " ":
            result_string += symbol
        else:
            default_symbol_index = letters_str.index(symbol)
            tmp_index = default_symbol_index + delta
            caesar_index = tmp_index if tmp_index < len_letters_str else tmp_index - len_letters_str
            result_string += letters_str[caesar_index]
    return result_string


if __name__ == '__main__':
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")