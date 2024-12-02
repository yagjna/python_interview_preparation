def merge(dict1, dict2):
    dict1.update(dict2)  # Updates dict1 with items from dict2
    print("The merged dictionary is:", dict1)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 1, 'd': 3}
merge(dict1, dict2)




#output :The merged dictionary is: {'a': 1, 'b': 2, 'c': 1, 'd': 3}
