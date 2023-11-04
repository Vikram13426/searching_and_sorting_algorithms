def partition(array, low, high):
    pivot = array[low]
    start = low+1
    end = high
    while start <= end:
        while array[end] > pivot:
            end -= 1
        while array[start] <= pivot:
            start += 1
       
        if start <= end:
            array[start], array[end] = array[end], array[start]
    array[low], array[end] = array[end], array[low]
    return end


def quick_sort(array, low, high):
    if low < high:
        loc = partition(array, low, high)
        quick_sort(array, low, loc-1)
        quick_sort(array, loc+1, high)
    return array




array = list(map(int, input("Enter the array elements to be sorted:").split()))
print("The array after sorted is :",quick_sort(array, 0, len(array)-1))

