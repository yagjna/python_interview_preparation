
# tuple packing
tup1 = 1, 2, 3
print('{}'.format(tup1))


#tuple unpacking
a, b, c = tup1
print('{}'.format(a))
print('{}'.format(b))
print('{}'.format(c))


#to count the occurance of elmemnt
tup2 = ('a', 1, 1, 3, 'f')
print('{}'.format(tup2.count('a')))


#to find the index of the element
print('{}'.format(tup2.index('f')))


#output:
(1, 2, 3)
1
2
3
1
4
