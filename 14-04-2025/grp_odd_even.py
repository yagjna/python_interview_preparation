
def grp_even_odd(lst1):
    even = []
    odd  = []

    dict1 = {}

    for x in lst1:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    dict1['even'] = even
    dict1['odd'] = odd

    return dict1

lst1 = [1, 2, 3, 4, 5]
print(grp_even_odd(lst1))

#output:{'even': [2, 4], 'odd': [1, 3, 5]}
