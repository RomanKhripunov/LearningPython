def checkio(*args):
    return max(args) - min(args) if args else 0

checkio2 =  lambda *x: max(x)-min(x) if x else 0

if __name__ == '__main__':
    import timeit
    # def almost_equal(checked, correct, significant_digits):
    #     precision = 0.1 ** significant_digits
    #     return correct - precision < checked < correct + precision
    #
    # assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    # assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    # assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    # assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    import random
    list_of_numbers = [random.randint(1, 60) for i in range(random.randint(1, 80))]
    print(id(list_of_numbers))
    print(timeit.timeit('checkio(*list_of_numbers)', setup='from __main__ import checkio, list_of_numbers', number=1000))
    print(id(list_of_numbers))
    print(timeit.timeit('checkio2(*list_of_numbers)', setup='from __main__ import checkio2, list_of_numbers', number=1000))

