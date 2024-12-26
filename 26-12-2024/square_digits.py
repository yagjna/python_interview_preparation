def square_digits(num):
    
    lst1 = []
    
    for x in str(num):
        square = int(x) **2
        lst1.append(str(square))
        
    return '-'.join(lst1)

num = '123'
print(square_digits(num))

#output:
1-4-9
