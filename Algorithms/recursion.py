# псевдокод код для нахождения ключа в шкатулках
def look_for_key(main_box):
    heap = main_box.values()
    while heap is not None:
        box = heap.pop()
        if isinstance(box, list):
            heap.append(box)
        elif isinstance(box, str):
            return box


def sum_elemtnts(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_elemtnts(arr[1:])


def count_elements(arr):
    return 1 + count_elements(arr[:-1]) if arr else 0


def max_value(arr):
    # max_val = 0
    # for i in arr:
    #     if i > max_val:
    #         max_val = i
    # return max_val
    if arr:
        return arr[0] if arr[0] > max_value(arr[1:]) else max_value(arr[1:])
    else:
        return 0


def binary_search(items_list, item):
    if len(items_list) == 1:
        guess = items_list[0]
        if guess == item:
            return items_list.index(guess)
        else:
            return None
    else:
        low, high = 0, len(items_list) - 1
        mid = (low + high) // 2
        guess = items_list[mid]
        if guess > item:
            binary_search(items_list[low:mid-1], item)
        else:
            binary_search(items_list[mid+1:high], item)


# my_list = [1, 3, 5, 9, 10, 11, 15, 55, 22, 24, 25, 29, 50, 56]
#
# print(binary_search(my_list, 55))

# s = "test"
# l1 = [1, 4, 5, 32, s, s, s]
# print(count_elements(l1))
#
# l2 = []
# print(sum_elemtnts(l2))

#
# l3 = [1, 44, 23, 5, 553, 23, 768]
# print(max_value(l3))
