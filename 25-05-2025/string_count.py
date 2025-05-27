"""
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []

"""
def friends_names(input):

    result = []
    for x in input:
        if len(x) == 4:
            result.append(x)
    return result


input = ["Ryan", "Kieran", "Jason", "Yous"]
print(friends_names(input))

#output : ['Ryan', 'Yous']
