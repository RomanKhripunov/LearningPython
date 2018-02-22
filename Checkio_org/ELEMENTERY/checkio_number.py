def checkio(number):
    buzz = "Buzz"
    fizz = "Fizz"
    if number % 5 == 0 and number % 3 == 0:
        return " ".join((fizz, buzz))
    elif number % 5 == 0:
        return buzz
    elif number % 3 == 0:
        return fizz
    else:
        return str(number)


if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

