def index_power(array, n):
    try:
        return array[n] ** n
    except IndexError:
        return -1


def index_power_2(array, n):
    return pow(array[n], n) if len(array) > n else -1


def index_power_3(array, n):
    return (len(array) <= n) * (-1) + (len(array) > n) * (array[min(iter(range(len(array))),
                                                                    key=lambda i: abs(i - n))] ** n)


if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"

    assert index_power_2([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power_2([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power_2([0, 1], 0) == 1, "Zero power"
    assert index_power_2([1, 2], 3) == -1, "IndexError"



