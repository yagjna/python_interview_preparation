

def largest_smallest(lst1):

    largest_num = lst1[0]
    smallest_num = lst1[0]

    for num in lst1:
        if num > largest_num:
            largest_num = num

        elif num < smallest_num:
            smallest_num = num

    return largest_num, smallest_num

lst1 = [12, 71, 90, 22, 77, 0, -1]
largest_num, smallest_num = largest_smallest(lst1)

print('the largest number in the list is: {}'.format(largest_num))
print('the smallest number in the list is: {}'.format(smallest_num))


"""
output: the largest number in the list is: 90
the smallest number in the list is: -1
"""
