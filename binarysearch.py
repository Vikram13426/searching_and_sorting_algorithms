def binary_search(l,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if array[mid]==key:
            return mid
        elif array[mid]>key:
            return binary_search(array,low,array[mid],key)
        else:
            return binary_search(array,array[mid]+1,key)
    else:
        return -1    
array=list(map(int,input("Enter the elements in the ascending order:").split()))
key=int(input("Enter the key you want to return index:"))
result=binary_search(array,0,len(array)-1,key)
print("The index of the key in the array is :",result)