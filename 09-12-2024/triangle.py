def is_triangle(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    
    
    return True

print(is_triangle(3, 4, 5))  
print(is_triangle(1, 1, 3))  
print(is_triangle(5, 7, 10)) 




#O/P : True
False
True
