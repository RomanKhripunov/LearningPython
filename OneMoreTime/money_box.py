import re

# make classes structure
class_count = int(input())
classes_dep = [re.split(" : | ", input()) for i in range(class_count)]
class_dict = {}

for dep in classes_dep:
    if len(dep) == 1:
        class_dict[dep[0]] = "object"
    else:
        class_dict[dep[0]] = dep[1:]


# read and execute queries
query_count = int(input())
query_struct = [input().split() for i in range(query_count)]


def check_class_is_parent(parent_name, child_name):
        def_parents_name = class_dict.get(child_name, None)
        res = "No"
        if def_parents_name:
            if parent_name in def_parents_name or parent_name == child_name:
                res = "Yes"
            else:
                for cls in def_parents_name:
                    if check_class_is_parent(parent_name, cls) == "Yes":
                        res = "Yes"
        return res


for query in query_struct:
    print(check_class_is_parent(query[0], query[1]))
