classes_dep = {}
exceptions_order = []


def create_class_dependencies():
    for _ in range(int(input())):
        tmp = input().split()
        classes_dep[tmp[0]] = tmp[2:] if len(tmp) > 1 else None


def create_exception_structure():
    for _ in range(int(input())):
        exceptions_order.append(input())


def print_unnecessary_exp():
    for exception_index, exception_name in enumerate(exceptions_order):
        if exception_index > get_min_parents_index(exception_index, exception_name):
            print(exception_name)


def get_min_parents_index(self_index, self_name):
    parent_list = classes_dep.get(self_name)
    if parent_list:
        tmp_min = self_index
        for parent in parent_list:
            if parent in exceptions_order:
                tmp_min = min(get_min_parents_index(get_class_index(parent), parent), tmp_min)
            else:
                tmp_min = min(get_min_parents_index(tmp_min, parent), tmp_min)
        return tmp_min
    else:
        return self_index


def get_class_index(class_name):
    return exceptions_order.index(class_name)


if __name__ == "__main__":
    create_class_dependencies()
    create_exception_structure()
    print_unnecessary_exp()
