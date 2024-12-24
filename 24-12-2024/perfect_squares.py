import math

def is_perfect_square(n):
    if n < 0:
        return False  
    sqrt_n = math.isqrt(n)  
    return sqrt_n * sqrt_n == n 


print(is_perfect_square(-1))  
print(is_perfect_square(0))   
print(is_perfect_square(3))   
print(is_perfect_square(4))   
print(is_perfect_square(25))  
print(is_perfect_square(26))  


#output:
False
True
False
True
True
False

