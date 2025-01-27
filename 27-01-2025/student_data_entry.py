
from random import *

def student_entry(id_characters):

    length = 6
    id_digits = []

    for x in range(length):
        id_digits.append(choice(id_characters))
    random_id = ''.join(id_digits)
    return random_id

def random_password(password_characters):

    length = 7
    password = ""

    for y in range(length):
        password = password + choice(password_characters)
    return password

def get_name(names):
    id_characters = '0123456789'
    password_characters = '0123456789!@#$%^&*'

    dict1 = {}
    for name in names:
        random_id = student_entry(id_characters)
        random_password_value = random_password(password_characters)
        dict1[name] = {'id': random_id, 'password': random_password_value}

    return dict1

id_characters = '0123456789'
password_characters = '0123456789!@#$%^&*'
names = ['honey', 'sweety', 'jaanu', 'bhuvi', 'geethanshi']

data = get_name(names)

print('{}'.format(data))


#output:
'honey': {'id': '139427', 'password': '%4*785%'}, 'sweety': {'id': '378450', 'password': '25*5!52'}, 'jaanu': {'id': '769890', 'password': '4%^###8'}, 'bhuvi': {'id': '666018', 'password': '7937%$*'}, 'geethanshi': {'id': '177117', 'password': '32*&305'}}
