def index_key(str1):
    str2 = str1.split(' ')
    dict1 = {}

    for index, key in enumerate(str2):
        dict1[index] = key

    return dict1

str1 = "learn python with fun"
dict1 = index_key(str1)
print('{}'.format(dict1))

'''
output : {0: 'learn', 1: 'python', 2: 'with', 3: 'fun'}
'''
