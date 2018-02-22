# a,b,c,d = (int(input()) for i in range(4))
# print(' ', *range(c, d+1), sep='\t')
# [ print(*[i, *range(i*c, i*d+1)], sep='\t') for i in range(a, b+1) ]
#
#
# items_list = ["apple", "melon", "watermelon"]
# print(items_list)
# print(*items_list)


# a, b = [i for i in input().split()], input()
# print(*[i for i, x in enumerate(a) if x == b]) if b in a else print("Отсутствует")


# n = int(input())
# n = 5
# l = [[k for k, j in enumerate(range(n))] for i in range(n)]
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(str(l[i][j]), end=" ")
#     print()
#
# big_list = [1, 2, 3, 4, 5, 6, 7]
# res_list = []
# rows = n
# cols = n
# for i in range(len(n)):
#     for j in range(len(n)):
#         res_list[i - rows][j - cols] = number


def spiral(n):
    dx, dy = 1, 0  # Starting increments
    x, y = 0, 0  # Starting location
    my_list = [[None] * n for j in range(n)]
    for i in range(n ** 2):
        my_list[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and my_list[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return my_list


def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=" ")
        print()


printspiral(spiral(5))



#
# ind = 1
# for i in range(n):
#     for j in range(n):
#         l.append([ind])
#



# a[i][j + 1]
# a[i][j + 2]
# a[i][j + 3]
# a[i][j + 4]
# a[i][j + 5]
# a[i][j + 6]
# a[i + 1][j]
# a[i + 2][j]
# a[i + 3][j]
# a[i + 4][j]
# a[i + 5][j]
# a[i + 6][j]
#
# a[i][j - 1]
# a[i][j - 2]
# a[i][j - 3]
# a[i][j - 3]
# a[i][j - 4]
# a[i][j - 5]
# a[i][j - 6]
# a[i - 1][j]
# a[i - 2][j]
# a[i - 3][j]
# a[i - 4][j]
# a[i - 5][j]
