def unique_in_order(sequence):
    
    lst1 = []
    
    for x in sequence:
        if x not in lst1:
            lst1.append(x)
            
    return lst1

sequence = 'AAAABBBCCDAABBB'

lst1 = unique_in_order(sequence)
print(lst1)
    
    
#output:
['A', 'B', 'C', 'D']
