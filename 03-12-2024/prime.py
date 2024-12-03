def prime(number):

    lst1 =[]

    for x in range(1,number+1):
        if number%x ==0:
            lst1.append(x)

    if len(lst1)==2:
        print("{}- is prime".format(x))
    else:
        print("{}-is composite".format(x))

number = eval(input('enter a number : '))
prime(number)

# output :
enter a number : 17
17- is prime

enter a number : 12
12-is composite

