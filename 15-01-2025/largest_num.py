
def largest_number(lst1):

    largest_number = lst1[0]

    for x in lst1:
        if x >largest_number:
            largest_number = x

    return largest_number

lst1 = [0, 72, 235, 27835, -1]
print(largest_number(lst1))

#output:
27835
