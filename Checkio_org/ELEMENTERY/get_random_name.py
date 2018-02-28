from random import randrange

for x in range(5):

    with open("names.txt") as file:
        names = file.read().replace(",", " ").replace(".", " ").replace("\n", " ").split()
        d = {}
        for i in range(100000):
            rand_num = randrange(len(names))
            d[names[rand_num]] = d[names[rand_num]] + 1 if names[rand_num] in d else 0
        print(str(max(d, key=d.get)))

