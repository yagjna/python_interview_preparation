my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# get elements from index 2 to 5
lst1 = my_list[2:6]
print("the elements from index 2 to 5 are : {}".format(lst1))

#to get every second element from index 1 to 8
lst2  = my_list[1:9:2]
print('every second element from index 1 to 8 are : {}'.format(lst2))

#to reverse the numbers in the list 
lst3 = my_list[::-1]
print('the reversed list is : {}'.format(lst3))



# output :the elements from index 2 to 5 are : [2, 3, 4, 5]
every second element from index 1 to 8 are : [1, 3, 5, 7]
the reversed list is : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

