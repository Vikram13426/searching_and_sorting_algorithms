

def selection_sort(array):
    length = len(array)
    for i in range(length-1):
        min_index = i
        for j in range(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
    return array

array = list(map(int, input("Enter the array elements to sort:").split()))
result = selection_sort(array)
print("The sorted array is :", result)
