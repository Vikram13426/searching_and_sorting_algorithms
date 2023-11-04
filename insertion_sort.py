def insertion_sort(array):
    for i in range(1,len(array)):
        temp=array[i]
        j=i-1
        while j>=0 and temp<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=temp
    return array        
            
array=list(map(int,input("Enter the array elements to sort :").split()))
result=insertion_sort(array)
print("The array after insertion_sort is :",result)