def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j< len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:] 
    result+=right[j:]
    return result
def merge_sort(array):
    if len(array)<= 1:
        return array
    mid=len(array)//2
    left=merge_sort(array[:mid])
    right=merge_sort(array[mid:])
    return merge(left,right)
array=list(map(int,input("ENter the array to be sorted:").split()))
print("The array after the merge sort is :",merge_sort(array))          