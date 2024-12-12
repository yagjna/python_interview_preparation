def array_diff(a, b):
    lst1 = []
    for x in a:
        if x not in b:
            lst1.append(x)
    return lst1

a = [1, 2]
b = [1]

lst1 = array_diff(a, b)

print(lst1)



#output: [2]
