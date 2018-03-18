def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        main_item = arr[0]
        less_items = [i for i in arr if i < main_item]
        great_items = [i for i in arr if i > main_item]
        return quick_sort(less_items) + [main_item] + quick_sort(great_items)


my_list = [1, 44, 3, 56, 2, 464, 112, 4, 0, 2, 4, 233, 29]
print(quick_sort(my_list))
