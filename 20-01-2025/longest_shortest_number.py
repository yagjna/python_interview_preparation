
def longest_shortest(lst1):
    longest = lst1[0]
    shortest = lst1[0]

    for x in lst1:
        if x >= longest:
            longest = x

    # for x in lst1:
        if x <= shortest:
            shortest = x

    return longest, shortest

lst1 = [1, 2, 3, 4, 5]
longest, shortest = longest_shortest(lst1)

print('the longest number is {}'.format(longest))

print("the shortest number is {}".format(shortest))

file_name = '20-01-2025.txt'

with open(file_name, 'a') as fh:
    fh.write('\n longest and shortest numbers:\n')
    fh.write(str(longest) + '\n')
    fh.write(str(shortest)+ '\n')

print('the file is added to - {}'.format(file_name))

#output:
the longest number is 5
the shortest number is 1
the file is added to - 20-01-2025.txt
