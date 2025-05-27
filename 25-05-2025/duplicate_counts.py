def count_duplicates(s):
    s = s.lower()  
    dict1 = {}

    for x in s:
        if x in dict1:
            dict1[x] = dict1[x] + 1
        else:
            dict1[1] = 1

    duplicate_count = 0
    for y in dict1.values():
        if y > 1:
            duplicate_count = duplicate_count + 1

    return duplicate_count

s = "aabBcde"
duplicate_count = count_duplicates(s)

print("{}".format(duplicate_count))



