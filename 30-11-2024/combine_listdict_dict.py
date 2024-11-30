def combine(lst1):

    dict1 = {}

    for x in lst1:
        for k, v in x.items():
            if k in dict1:
                dict1[k] = dict1[k] +v
            else:
                dict1[k] = v

    return dict1

lst1 = [{'a':1, 'b':2},{'b':3,'c':4},{'a':5,'c':6}]
dict1 = combine(lst1)
print("the combined dictionary is: {}".format(dict1))



#output : the combined dictionary is: {'a': 6, 'b': 5, 'c': 10}
