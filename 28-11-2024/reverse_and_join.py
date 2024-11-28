def reverse(str1):
    # Split the string into words
    str2 = str1.split()  # Correctly assign str1.split() to str2
    lst1 = []  # Initialize an empty list for reversed words

    # Reverse each word and add it to lst1
    for x in str2:
        y = x[::-1]  # Reverse the word
        lst1.append(y)  # Append the reversed word to the list

    # Join the reversed words with spaces and return the result
    return ' '.join(lst1)

str1 = 'this is'
lst1 = reverse(str1)
print(lst1)




output:
    siht si
