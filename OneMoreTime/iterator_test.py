from __future__ import print_function

# Six представляет родительский класс,
# который позволяет не думать, какой next-метод объявлять в объекте,
# — это всегда __next__()
# from six import Iterator

test = I
class MyIterator(Iterator):
    def __init__(self, step=5):
        self.step = step


    def __iter__(self):
        return self


    def __next__(self):
        self.step -= 1
        #Условие остановки итератора, чтобы он не бежал вечно
        if not self.step:
            raise StopIteration()
        return self.step

myiterator = MyIterator()
for item in myiterator:
    print(item, end=" ")
    print()


def my_generator():
    with open("file.txt", "r") as f:
        for l in f:
            if "foo" in l:
                yield l

myiterator = my_generator()
for item in myiterator:
    print(item)
    



def my_generator2():
    print("First block") 
    yield 1
    print("Second block")
    yield 2

myiterator = my_generator2()
myiterator.next() #"First block"
myiterator.next() #"Second block"
myiterator.next() #Traceback: StopIteration









wwwlog = open("access-log")
bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')
print("Total", sum(bytes))