n = eval(input('enter no.of rows:'))

for x in range(n):
    for y in range(n - x):
        print(y + 1, end = ' ')

    print()


#output :

enter no.of rows:3
1 2 3
1 2
1
