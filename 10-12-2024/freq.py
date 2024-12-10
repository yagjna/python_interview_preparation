def most_frequent(lst1):
    # Dictionary to store frequencies
    dict1 = {}
    for x in lst1:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1

    # Find the most frequent element manually
    max_count = 0
    most_frequent_element = None

    for k, v in dict1.items():
        if v > max_count:
            max_count = v
            most_frequent_element = k

    print(f"The most frequent element is '{most_frequent_element}' with a frequency of {max_count}.")

# Example list
lst1 = ['geeks', 'for', 'geeks', 'is', 'for', 'for']
most_frequent(lst1)



#output : The most frequent element is 'for' with a frequency of 3.

