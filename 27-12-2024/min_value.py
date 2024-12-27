def min_value(digits):
    
    lst1 =[]
    
    for x in digits:
        if x not in lst1:
            lst1.append(x)
    lst1.sort()
    return ''.join(map(str, lst1))

digits = [1, 2, 1, 3]
print(min_value(digits))

#output:
123
