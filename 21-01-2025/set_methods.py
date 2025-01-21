
#to add a element to set
set1 = {1, 2, 'a', 'z'}

set1.add(5)
print('{}'.format(set1))

#to remove a element and return that element'
print('{}'.format(set1.pop()))

#to remove a particular element
set1.remove(2)
print('{}'.format(set1))

#to add 2 sets
set2 = {3, 4, 'b', 'y',1}
print(set1.union(set2))

print(set1.intersection(set2))


#output:
{1, 2, 5, 'a', 'z'}
1
{5, 'a', 'z'}
{'y', 1, 3, 4, 5, 'b', 'a', 'z'}
set()
