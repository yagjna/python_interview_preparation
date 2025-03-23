
def largest_number(lst1):

    largest = lst1[0]

    for x in lst1:
        if x > largest:
            largest = x

    return largest

lst1 = [1,5,11,8]
print(largest_number(lst1))

#output: 11
