
lst1 = [1, 2, 3, 4, 5]

for x in lst1:
    print(x, end = ' ')


file_name = 'list_num.txt'
with open('file_name', 'w') as fh:
    fh.write("{}\n".format(x))


print("The prime numbers have been saved to '{}'.".format(file_name))
