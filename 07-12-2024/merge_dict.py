
import pdb;pdb.set_trace()

dict1 = {"a":1, "b":2, "c":3}

dict2 = {"frits":"apple", "vegetables":"xyz"}

#to merge two dictionaries 

dict3 = {**dict1,**dict2}

print("{}".format(dict3))




#output : {'a': 1, 'b': 2, 'c': 3, 'frits': 'apple', 'vegetables': 'xyz'}
