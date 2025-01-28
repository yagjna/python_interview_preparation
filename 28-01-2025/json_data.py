
import json

data = {
    'name' : 'yagjna',
    'age' : 23,
    'languages_known' : ['telugu', 'english', 'hindi'],
    'address' : {
        'city' : 'kakinada',
        'phone_number' : 987654321,
    }
}

file_name = 'data.json'

with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=5)
    print(data)


#output:
{'name': 'yagjna', 'age': 23, 'languages_known': ['telugu', 'english', 'hindi'], 'address': {'city': 'kakinada', 'phone_number': 987654321}}
