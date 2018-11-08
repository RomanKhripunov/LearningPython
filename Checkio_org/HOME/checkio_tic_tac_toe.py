print_count = 1

def return_wrapper(func):
    def wrapper(*args, **kwargs):
        global print_count
        result = func(*args, **kwargs)
        print(print_count, result)
        print_count += 1
        return result
    return wrapper

@return_wrapper
def checkio(matrix):
    available_symbols = ('X', 'O')

    for tmp_matrix in (matrix, list(zip(*matrix))):
        matrix_len = len(tmp_matrix)
        copied_matrix = tmp_matrix.copy()

        tmp1 = ''
        tmp2 = ''
        for i in range(matrix_len):
            tmp1 += tmp_matrix[i][i]
            tmp2 += tmp_matrix[i][matrix_len - i - 1]
        copied_matrix.extend((tmp1, tmp2))

        for i in copied_matrix:
            if len(set(i)) == 1 and i[0] in available_symbols:
                return i[0]

    return 'D'


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio([
        "X.X",
        "OOO",
        "O.."]) == "O", "Os wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


