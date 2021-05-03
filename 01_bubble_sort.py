
array = [ 3, 2, 4, 1, 6, 8, 4, 3 ]
smallest = 0

for i in range(len(array)):
    smallest = i
    for j in range(i, len(array)):
        if array[j] < array[smallest]:
            smallest = j
    array[smallest], array[i] = array[i], array[smallest] # swap two elements
print (array)
