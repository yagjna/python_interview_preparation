def odd_or_even(arr):
    sum_arr = sum(arr)  
    if sum_arr % 2 == 0:  
        return "even"
    else:  
        return "odd"


arr = [0, 1, 4]
print(odd_or_even(arr))  

arr = [0]
print(odd_or_even(arr)) 

arr = [0, -1, -5]
print(odd_or_even(arr))  


#output:
odd
even
even
