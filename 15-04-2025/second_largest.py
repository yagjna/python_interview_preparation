
import pdb;pdb.set_trace()

def second_largest_number(lst1):

    first_largest = lst1[0]

    for x in lst1:
        if x > first_largest:
            first_largest = x

    second_largest = lst1[0]

    for y in lst1:
        if y > second_largest and y != first_largest:
            second_largest = y

    return second_largest

lst1 = [1, 2, 4, 28, 5, 8, 11]
second_largest =  second_largest_number(lst1)

print("the second largest number in the list is: {}".format(second_largest))

#output:the second largest number in the list is: 11
