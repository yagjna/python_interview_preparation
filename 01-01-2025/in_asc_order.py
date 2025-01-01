def in_asc_order(arr):
    
    if arr == sorted(arr):
        return True
    else:
        return False
    
arr = [1,2,4,7,19]
print(in_asc_order(arr))

arr = [1,6,10,18,2,4,20]
print(in_asc_order(arr))


#output:
True
False
