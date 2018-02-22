import os


def func(*args):
    [print(i) for i in args]

homeDirectory = "LearningPython"

func(*open(os.path.join(os.path.expanduser('~'), homeDirectory, "myfile.txt")))