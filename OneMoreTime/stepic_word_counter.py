import os


result_dict = {}
with open(os.path.join(os.path.expanduser('~'), "Downloads", "dataset_3363_3.txt")) as input_file:
    for line in input_file:
        tmp_list = line.strip().lower().split()
        for word in set(tmp_list):
            if word not in result_dict:
                result_dict[word] = tmp_list.count(word)
            else:
                result_dict[word] += tmp_list.count(word)

with open("result_stepic.txt", "w") as output_file:
    result_key = min([k for k, v in result_dict.items() if v == max(result_dict.values())])
    output_file.write(str(result_key) + " " + str(result_dict[result_key]))
