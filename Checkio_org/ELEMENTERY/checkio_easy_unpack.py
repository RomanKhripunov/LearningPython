def easy_unpack(elements):
    return elements[0], elements[2], elements[-2]


def easy_unpack_2(elements):
    return tuple(elements[i] for i in (0, 2, -2))


if __name__ == '__main__':
    import time

    start = time.time()
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    end = time.time()
    print("{:0.7f}".format(end - start))

    start = time.time()
    assert easy_unpack_2((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack_2((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack_2((6, 3, 7)) == (6, 7, 3)
    end = time.time()
    print("{:0.7f}".format(end - start))
