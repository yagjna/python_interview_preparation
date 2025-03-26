
def index(lst1):

    dict1 = {}

    for x in lst1:
        dict1[x] = lst1.index(x)

    return dict1

lst1 = ['apple', 'banana', 'cherry']
dict1 = index(lst1)

print('the index is - {}'.format(dict1))

"""
output: the index is - {'apple': 0, 'banana': 1, 'cherry': 2}g
"""
