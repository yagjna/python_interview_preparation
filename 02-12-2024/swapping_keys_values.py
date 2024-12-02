def key_values(dict1):
    dict2 = {}
    for k, v in dict1.items():  # Iterate over key-value pairs using .items()
        dict2[v] = k  # Assign value 'v' as the key, and key 'k' as the value
    return dict2

dict1 = {'hello': 1, 'world': 2, 'how': 3, 'are': 4, 'you': 5}
dict2 = key_values(dict1)
print('The dictionary after swapping keys and values is {}'.format(dict2))




#output: The dictionary after swapping keys and values is {1: 'hello', 2: 'world', 3: 'how', 4: 'are', 5: 'you'}
