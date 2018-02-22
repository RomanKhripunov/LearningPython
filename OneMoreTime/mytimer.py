import time
reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kwargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kwargs)
    elapsed = time.clock() - start
    return elapsed, ret


def my_list_iterator_1():
    l = []
    for i in range(10000):
        l.append(i)
    return l


def my_list_iterator_2():
    return [i for i in range(10000)]

print(timer(my_list_iterator_1)[0])
print(timer(my_list_iterator_2)[0])