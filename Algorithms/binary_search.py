def binary_search(items_list, item):
    low, high = 0, len(items_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = items_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 9, 10, 11, 15, 22, 24, 25, 29, 50, 56]

print(binary_search(my_list, 55))
print(binary_search(my_list, -1))
