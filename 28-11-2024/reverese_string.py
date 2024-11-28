def reverse(lst1):
    lst2 = []
    for x in lst1:
        y= x[::-1]
        lst2.append(y)
    return lst2 
lst1 = ['geeks','for','geeks']
x = reverse(lst1)
print(x)
def empty(lst1):
    lst3 = []  # List to store empty lists
    for sublist in lst1:  # Iterate through each sublist in lst1
        if sublist != []:  # Check if the sublist is empty
            lst3.append(sublist)  # Add it to lst3
    return lst3  # Return the list of empty lists

lst1 = [[1, 2], [], [3, 4]]
lst = empty(lst1)
print(lst)




output:
    ['skeeg', 'rof', 'skeeg']
[[1, 2], [3, 4]]
