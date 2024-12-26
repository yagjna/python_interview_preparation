def max_multiple(divisor, bound):
    
     for x in range(bound, 0, -1):
        if x % divisor == 0:
            return x  

divisor, bound = 6, 7
print(max_multiple(divisor, bound))  

divisor, bound = 10, 50
print(max_multiple(divisor, bound)) 

#output:
6
50
