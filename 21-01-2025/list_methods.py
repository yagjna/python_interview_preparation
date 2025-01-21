
# to add a element at the end of the list
lst1 = [1, 2, 'a', 'b']
lst1.append(3)

print('{}'.format(lst1))



#to extend the list
lst2 = ['d', 5]
lst1.extend(lst2)

print('{}'.format(lst1))
print('{}'.format(lst2))



#to insert a element at particular index
lst1.insert(2, 'f')
print('{}'.format(lst1))


#to remove a paricular element form the list
lst2.remove(5)
print('{}'.format(lst2))

#to remove the last element and return that element
print('{}'.format(lst1.pop()))

#to clear the list
lst2.clear()
print('{}'.format(lst2))


#to get a list in ascending order
lst3 = [1, 5, 3, 7]
lst3.sort()
print('{}'.format(lst3))

#output:
[1, 2, 'a', 'b', 3]
[1, 2, 'a', 'b', 3, 'd', 5]
['d', 5]
[1, 2, 'f', 'a', 'b', 3, 'd', 5]
['d']
5
[]
[1, 3, 5, 7]
