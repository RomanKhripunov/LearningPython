def checkio(expression):
    left_brackets = ('(', '{', '[')
    right_brackets = {')': left_brackets[0], '}': left_brackets[1], ']': left_brackets[2]}

    brackets_only = [ch for ch in expression if ch in left_brackets or ch in right_brackets]

    queue_brackets = []

    if len(brackets_only) == 0:
        return True

    if len(brackets_only) % 2 != 0:
        return False

    for symbol in brackets_only:
        if symbol in left_brackets:
            queue_brackets.append(symbol)
        elif symbol in right_brackets and len(queue_brackets) > 0 and queue_brackets[-1] == right_brackets[symbol]:
            queue_brackets.pop()

    return not queue_brackets


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("[{}]]") == False, "Failed in checkio"
    assert checkio("[1+202]*3*({4+3)}") == False, "Failed in checkio"
