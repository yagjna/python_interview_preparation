
def longest_shortest(lst1):
    longest = lst1[0]
    shortest = lst1[0]  # Corrected typo here
    for x in lst1:
        if len(x) > len(longest):
            longest = x
    for y in lst1:
        if len(y) < len(shortest):
            shortest = y
    return longest, shortest

lst1 = ['cat', 'elephant', 'bat', 'whale']
longest, shortest = longest_shortest(lst1)
print('The longest word in the list is: {}'.format(longest))
print('The shortest word in the list is: {}'.format(shortest))


output:
    The longest word in the list is: elephant
The shortest word in the list is: cat
