def variable_length(lst1):
    dict1 = {}
    for x in lst1:
        dict1[x] = len(x)  # Add the word and its length to the dictionary

    result = []
    for k, v in dict1.items():
        result.append(f"('{k}', {v})")  # Format each key-value pair as a string

    return ', '.join(result)  # Join all formatted strings with a comma and space

lst1 = ['python', 'is', 'easy']
result = variable_length(lst1)
print(result)




#output :('python', 6), ('is', 2), ('easy', 4)
