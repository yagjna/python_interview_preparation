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


file_name = 'longest_shortest.txt'
with open('file_name', 'w') as fh:
    fh.write("the largest number in the list is: {}\n".format(largest_num))
    fh.write("the smallest number in the list is: {}\n".format(smallest_num))

print("The prime numbers have been saved to '{}'.".format(file_name))


#output:
the largest number in the list is: 90
the smallest number in the list is: -1
The prime numbers have been saved to 'longest_shortest.txt'.

