import random

arr_size = 10
array = [random.randint(0, 10) for i in range(arr_size)]

def quicksort(array):
    array_size = len(array)
    if array_size <= 1:
        return array
    if array_size == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        middle = array[0]
        less = [i for i in array[1:] if i <= middle]
        more = [i for i in array[1:] if i > middle]
        return quicksort(less) + [middle] + quicksort(more)

print(quicksort(array))
