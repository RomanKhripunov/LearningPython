def second_index(text: str, symbol: str):
    return text.index(symbol, text.index(symbol) + 1) if text.count(symbol) > 1 else None


if __name__ == '__main__':
    assert second_index("My little example", "l") == 7, "Another"
    assert second_index("simses", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
