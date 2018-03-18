def find_smallest(arr):
    smallest_val = arr[0]
    smallest_ind = 0
    for i in range(1, len(arr)):
        if smallest_val > arr[i]:
            smallest_val = arr[i]
            smallest_ind = i
    return smallest_ind


def selection_sort(arr):
    result_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        result_arr.append(arr.pop(smallest))
    return result_arr


l = [1, 3, 7, 5, 9, 4, 6, 7, 8, 0, 4, 2, 6]
print(selection_sort(l))

