def binary_array_to_number(arr):
    
    result = 0
    
    for x in arr:
        result = result * 2 + x
        
    return result

arr = [0, 0, 0, 1]
print(binary_array_to_number(arr))

arr = [0, 0, 1, 0]
print(binary_array_to_number(arr))


#output:
1
2
