def two_oldest_ages(ages):
    largest_first = ages[0]
    largest_second = ages[0]
    lst1 = []
    
    for x in ages:
        if x > largest_first:
            largest_second = largest_first
            largest_first = x
        elif x > largest_second and x != largest_first:
            largest_second = x
            
    lst1.append(largest_first)
    lst1.append(largest_second)
    
    return sorted(lst1)  

ages = [1, 5, 87, 45, 8, 8]
print(two_oldest_ages(ages))


#output:
[45, 87]
