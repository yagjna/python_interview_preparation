
# Merge two dictionaries and sum values for common keys

def merged_key_sum(dict1, dict2):

    merged_dict = {}

    for key, value in dict1.items():
        merged_dict[key] = value

    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value

    return merged_dict

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 40}

merged_dict = merged_key_sum(dict1, dict2)

print(' the sum of common keys is - {} '.format(merged_dict))

'''
output : the sum of common keys is - {'a': 10, 'b': 35, 'c': 55, 'd': 40}

'''
