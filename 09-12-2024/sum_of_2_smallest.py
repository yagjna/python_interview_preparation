def sum_two_smallest_numbers(numbers):
    
    shortest1 = numbers[0]
    shortest2 = numbers[0]

    for x in numbers:
        if x < shortest1:
    
            shortest2 = shortest1
        
            shortest1 = x
        elif x < shortest2:
        
            shortest2 = x
    
    
    return shortest1 + shortest2


numbers = [19, 5, 42, 2, 77]
result = sum_two_smallest_numbers(numbers)
print('sum_two_smallest_numbers_is : {}'.format(result))




#output : sum_two_smallest_numbers_is : 7
