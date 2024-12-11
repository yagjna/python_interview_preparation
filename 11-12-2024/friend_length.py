#Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []



def friend(x):
    lst1 = []
    for word in x:
        if len(word) == 4:
            lst1.append(word)
    return lst1

x = ["Ryan", "Kieran", "Jason", "Yous"]

lst1 = friend(x)
print(lst1)




#output:
    ['Ryan', 'Yous']
