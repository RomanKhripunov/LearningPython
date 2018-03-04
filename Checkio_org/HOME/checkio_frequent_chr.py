def checkio(text):
    tmp_dict = {chr: text.lower().count(chr) for chr in set(text.lower()) if chr.isalpha()}
    return max(sorted(tmp_dict), key=tmp_dict.get)


def checkio_2(text):
    text_filtered = list(filter(lambda x: x.isalpha(), sorted(text.lower())))
    return max(text_filtered, key=text_filtered.count)


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

