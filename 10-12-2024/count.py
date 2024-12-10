def count(str1):
    # Dictionary to store word frequencies
    dict1 = {}
    
    # Split the string into words
    words = str1.split(' ')
    
    # Count the occurrences of each word
    for word in words:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1

    # Return the dictionary
    return dict1

# Input string
str1 = 'geeks for geeks'
result = count(str1)

# Print the word frequencies
for k, v in result.items():
    print(k, v)





#output : geeks 2
for 1

