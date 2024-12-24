def get_even_numbers(arr):
    
    lst1 = []
    
    for x in arr:
        if x % 2 == 0:
            lst1.append(x)
            
    return lst1

arr = ([2,4,5,6])
print(get_even_numbers(arr))


#output: [2, 4, 6]
