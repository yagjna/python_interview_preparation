def largest_pair_sum(numbers): 
    
    sum = 0
    first_largest = numbers[0]
    second_largest = numbers[0]

    for x in numbers:
        if x > first_largest:
            first_largest = x
            
    for x in numbers:
        if x > second_largest and x < first_largest:
            second_largest = x
            
    sum  = first_largest + second_largest
    
    return sum 

numbers = [10, 14, 2, 23, 19]
print(largest_pair_sum(numbers))



#output:
42
