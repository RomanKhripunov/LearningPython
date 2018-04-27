def long_repeat(line):
    tmp_char = None
    current_count = 0
    int_list = []
    for ind, ch in enumerate(line):
        if tmp_char is None:
            tmp_char = ch
            current_count = 1
        elif ch != tmp_char:
            int_list.append(current_count)
            tmp_char = ch
            current_count = 1
        else:
            current_count += 1
    return max(int_list) if line else 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

