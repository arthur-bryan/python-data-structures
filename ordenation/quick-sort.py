import timeit


def partition(array, low, high):
    s_index = (low-1)  # smaller element index
    pivot = (array[high] + array[low]) / 2
    for i in range(low, high):
        if array[i] <= pivot:
            s_index = s_index+1
            array[s_index], array[i] = array[i], array[s_index]
    array[s_index+1], array[high] = array[high], array[s_index+1]
    return (s_index+1)


def quick_sort(array, low, high):
    if len(array) == 1:
        return arry
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)


