def descending_order(n):
    
    digits = list(str(n))
    
    sorted_digits = sorted(digits, reverse=True)
    
    result = int("".join(sorted_digits))
    return result


print(descending_order(42145))        
print(descending_order(145263))      
print(descending_order(123456789))   


#output :
54421
654321
98765421
