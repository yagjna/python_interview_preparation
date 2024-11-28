
def duplicates(lst1):
    lst2 = []  # To store duplicate elements
    seen = []  # To track already seen elements

    for x in lst1:
        if x in seen:
            if x not in lst2:
               lst2.append(x)  # Add to duplicates if already in seen and not in lst2
        else:
            seen.append(x)  # Add to seen for the first time
    return lst2

lst1 = [1, 2, 2, 3, 4, 5, 3, 1]
lst2 = duplicates(lst1)
print(lst2)




output:
    [2, 3, 1]
