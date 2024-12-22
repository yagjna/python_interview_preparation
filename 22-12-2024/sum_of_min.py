def sum_of_minimums(numbers):
    total_sum = 0
    for row in matrix:
        min_value = min(row)
        
        total_sum += min_value

    
    return total_sum


matrix = [
    [1, 2, 3, 4, 5],       
    [5, 6, 7, 8, 9],      
    [20, 21, 34, 56, 100]  
]
print(sum_of_minimums(matrix))  


#output:
26
