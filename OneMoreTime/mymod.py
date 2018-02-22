def count_lines(file):
    file.seek(0)
    return len(file.readlines())


def count_chars(file):
    file.seek(0)
    return len(file.read())


def test(name):
    with open(name) as file:
        return count_lines(file), count_chars(file)


if __name__ == "__main__":
    print(test("mymod.py"))