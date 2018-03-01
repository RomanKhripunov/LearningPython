def checkio(number):
    from functools import reduce
    return reduce(lambda res, x: res * x, filter(None, [int(i) for i in str(number)]))


def checkio_2(number):
    from functools import reduce
    from operator import mul
    return reduce(mul, filter(None, map(int, str(number))))


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

