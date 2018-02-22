#
# result_list = []
# with open("dataset_3363_4.txt") as input_file:
#     for line in input_file:
#         tmp_list = line.strip().split(";")
#         result_list.append([tmp_list[0], tmp_list[1:]])
#
# print(result_list)
#
# with open("result_stepic.txt", "w") as output_file:
#     for student_data in result_list:
#         sum_number = 0
#         for number in student_data[1]:
#             sum_number += int(number)
#         avg = sum_number / len(student_data[1])
#         if avg % 1 == 0:
#             output_file.write(str(avg))
#         else:
#             output_file.write("{:.9f}".format(avg))
#         output_file.write("\n")
#
#     total_list = [[0, 0], [0, 0], [0,0]]
#     for student_data in result_list:
#         sum_number = 0
#         for ind, number in enumerate(student_data[1]):
#             total_list[ind][0] += int(number)
#             total_list[ind][1] += 1
#     for x in total_list:
#         avg = x[0] / len(s)
#         if avg % 1 == 0:
#             output_file.write(str(avg))
#         else:
#             output_file.write("{:.9f}".format(avg))
#         output_file.write(" ")

import sys
import statistics
f = sys.stdin
l = [list(map(float, l.strip().split(";")[1:])) for l in f]
print(*[statistics.mean(s) for s in l], sep="\n")
print(*[statistics.mean(i) for i in zip(*l)])