
def reverse_str(lst1):

    lst2 = []

    for x in lst1:
        y = x[::-1]
        lst2.append(y)

    return lst2 

lst1 = ['hello', 'world', 'how', 'are', 'you']
lst2 = reverse_str(lst1)

print("the reversed strings in the list are : {}".format(lst2))









#output :

the reversed strings in the list are : ['olleh', 'dlrow', 'woh', 'era', 'uoy']
