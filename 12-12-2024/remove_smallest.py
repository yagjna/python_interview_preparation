def remove_smallest(numbers):
    if not numbers: 
        return []
    
    smallest = min(numbers)  
    lst1 = []  
    removed = False  
    
    for x in numbers:
        if x == smallest and not removed:  
            removed = True
        else:
            lst1.append(x)
    
    return lst1

# Example usage
numbers = [1, 1, 2, 3, 4]
result = remove_smallest(numbers)

print('The list after removing the smallest is: {}'.format(result))



#output :
The list after removing the smallest is: [1, 2, 3, 4]
