
def fabonicci(n):

    a, b = 0, 1

    lst1 = []
    for x in range(n):
        lst1.append(a)

        a, b = b, a+b

    return lst1

n = eval(input('enter n value : '))
lst1 = fabonicci(n)

print("the series is : {}".format(lst1))

file_name = 'list_count.txt'
with open(file_name, 'a') as fh:
    fh.write("\nFibonacci series:\n")
    fh.write(str(lst1) + "\n")

print('fabnocci series file added to - {}'.format(file_name))
