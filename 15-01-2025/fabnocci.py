
def fabnocci_series(num):

    a, b = 0, 1

    lst1 = []

    for x in range(num):
        lst1.append(a)

        a, b = b, a + b

    return lst1

num = eval(input('enter a number : '))
print(fabnocci_series(num))

#output:
enter a number : 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
