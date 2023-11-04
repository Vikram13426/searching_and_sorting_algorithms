def linear_search(array,key):
    for i in range(len(array)):
        if array[i]==key:
            return i
        else:
            continue
array=list(map(int,input("Enter the elements in the array:").split()))
key=int(input("Enter the key you want to find the index:"))
result=linear_search(array,key)
print("The index of the key is:",result)