def divisors(integer):
    
    lst1 = []
    
    for x in range(2, integer):
        if integer % x == 0:
            lst1.append(x)
    
    if len(lst1) == 0:
        return '{} is prime'.format(integer)
    else:
        return lst1  

print(divisors(12))  


#output :
[2, 3, 4, 6]
