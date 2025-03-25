
import pdb;pdb.set_trace()

def merge_dict_sum(data):

    dict1 = {}

    for x in data:
        for key, values in x.items():
            if key in dict1:
                dict1[key] = dict1[key] + values
            else:
                dict1[key] = values

    return dict1

data = [{'a': 10, 'b': 20}, {'a': 5, 'b': 15, 'c': 25}]
dict1 = merge_dict_sum(data)

print('the merged values sum is - {}'.format(dict1))
