# Bubble Sort Exercise
# Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

# bubble_sort(elements, key='transaction_amount')
# This will sort elements by transaction_amount and your sorted list will look like,

# elements = [
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
# But if you call it like this,

# bubble_sort(elements, key='name')
# output will be,

# elements = [
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]



def bubble_sort(elements,key=''):
    length=len(elements)
    for i in range(length):
        swapped=False
        for j in range(length-i-1):
            if elements[j][key]>elements[j+1][key]:
               elements[j],elements[j+1]=elements[j+1],elements[j]
               swapped=True
        if not swapped:
            break 
    return elements          
elements = [{'name': 'mona',
            't': 1000,
             'd': 'iphone'}, {'name': 'dhaval',
                              't': 400,
                              'd': 'gpixel'},
            {'name': 'kathy',
            't': 200,
             'd': 'vivo'},
            {'name': 'amir',
            't': 800,
             'd': 'iphone-8'}]
result=bubble_sort(elements,key='d')
print(result)
