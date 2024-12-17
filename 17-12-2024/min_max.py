def min_max(lst):
    lst1 = []
    x = min(lst)
    y = max(lst)
    
    return [x, y]

lst = [1, 2, 3, 4, 5]
lst1 = min_max(lst)

print(lst1)


#output:
[1, 5]
