def most_frequent(data):
    d = {s: data.count(s) for s in set(data)}
    return max(d, key=d.get)


def most_frequent_2(data):
    d = {}
    for i in data:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return max(d, key=d.get)


if __name__ == '__main__':
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

