# [i for i in input().split()]
my_list = []
while True:
    s = input()
    if s == "end":
        break
    my_list.append(s.split())

for i in my_list:
    print(i)

result_list = my_list[:][:]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        summ = 0
        for r in [1, -1]:
            dj = j + r if (j + r) < len(my_list[i]) else 0
            summ += int(my_list[i][dj])
        for c in [1, -1]:
            di = i + c if (i + c) < len(my_list) else 0
            summ += int(my_list[di][j])
        result_list[i][j] = summ


for i in result_list:
    print(i)