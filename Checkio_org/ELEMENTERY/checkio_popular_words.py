def popular_words_1(text, words):
    lower_text = text.lower()
    return {word: lower_text.count(word) for word in words}


def popular_words_2(text, words):
    return {word: text.lower().count(word) for word in words}


import re
def popular_words_3(text, words):
    text = text.lower()
    text = re.split('\n|,| |\.', text)
    count = {}
    for word in words:
        count[word] = 0
        for k in text:
            if word == k:
                count[word] = count[word] + 1
    return count


if __name__ == '__main__':
    import time

    for method in (popular_words_1, popular_words_2, popular_words_3,):
        elapsed_time_list = []
        for i in range(100):
            start = time.time()
            assert popular_words_1('''
        When I was One,
        I had just begun.
        When I was Two,
        I was nearly new.
        ''', ['i', 'was', 'three']) == {
                'i': 4,
                'was': 3,
                'three': 0
            }
            end = time.time()
            elapsed_time = end - start
            elapsed_time_list.append(elapsed_time)
        avg = sum(elapsed_time_list) / len(elapsed_time_list)
        print(str(method.__name__) + " took: {:.7f}".format(avg))
