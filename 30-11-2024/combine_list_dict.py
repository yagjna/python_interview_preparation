def combine(key, values):

    result = dict(zip(key, values))
    return result

key = ['a', 'b', 'c']
values = [1, 2, 3]
result = combine(key, values)
print("the combined dict is {}".format(result))

 

 # output : the combined dict is {'a': 1, 'b': 2, 'c': 3}
