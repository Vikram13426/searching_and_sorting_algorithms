def bubble_sort(a):       
    length=len(a)         
    for i in range(length):
        swapped=False
        for j in range(length-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if not swapped:
            break      
    return a                 
a=list(map(int,input("Enter the elements in the list:").split()))
result=bubble_sort(a)
print("The sorted a is :",result)