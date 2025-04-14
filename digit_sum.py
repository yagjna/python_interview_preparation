def digital_root(n):
    while n >= 10:
        
        n_str = str(n)
        
        digit_sum = 0
        
        for digit in n_str:
            digit_sum += int(digit)
        
        n = digit_sum
    
    return n


print(digital_root(16))       
print(digital_root(942))      
print(digital_root(132189))   
print(digital_root(493193))   


#output:
7
6
6
2
