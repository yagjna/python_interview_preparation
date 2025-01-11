
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


#output:
enter n value : 6
the series is : [0, 1, 1, 2, 3, 5]
