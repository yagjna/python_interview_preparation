def comp(a, b):
    
    if a is None or b is None:
        return False
    squared_a = sorted([x * x for x in a])
    sorted_b = sorted(b)
    return squared_a == sorted_b


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b)) 

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))  

a = None
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))



#output:
True
False
False
