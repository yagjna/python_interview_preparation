def divisors(n):
    lst1 = []

    for x in range(1, n + 1):
        if n % x == 0:
            lst1.append(x)

    string_divisors = []
    for num in lst1:
        string_divisors.append(str(num))

    divisor_str = ', '.join(string_divisors)

    length = len(lst1)

    print('We have {} divisors - {}'.format(length, divisor_str))

    return length


print(divisors(1))  


#output:
We have 1 divisors - 1
1
We have 3 divisors - 1, 2, 4
3
We have 2 divisors - 1, 5
2
We have 6 divisors - 1, 2, 3, 4, 6, 12
6
We have 8 divisors - 1, 2, 3, 5, 6, 10, 15, 30
8
We have 13 divisors - 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096
13
