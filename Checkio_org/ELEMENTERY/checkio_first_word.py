import re
import time



def first_word_1(text: str) -> str:
    for ch in [",", "."]:
        text = text.replace(ch, "")
    return text.split()[0]


def first_word_2(text: str) -> str:
    return re.search("([\w']+)", text).group(1)


def first_word_3(text: str) -> str:
    return text.replace('.', ' ').replace(',', ' ').split()[0]


def first_word_4(text: str) -> str:
    return re.findall(r"[\w']+", text)[0]


if __name__ == '__main__':
    for method in (first_word_1, first_word_2, first_word_3, first_word_4):
        elapsed_time_list = []
        for i in range(100):
            start = time.time()

            assert method("Hello world") == "Hello"
            assert method(" a word ") == "a"
            assert method("don't touch it") == "don't"
            assert method("greetings, friends") == "greetings"
            assert method("... and so on ...") == "and"
            assert method("hi") == "hi"

            end = time.time()
            elapsed_time = end - start
            elapsed_time_list.append(elapsed_time)
        avg = sum(elapsed_time_list) / len(elapsed_time_list)
        print(str(method.__name__) + " took: {:.7f}".format(avg))

