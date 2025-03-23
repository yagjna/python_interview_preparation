
import pdb;pdb.set_trace()

def prime_number(number):

    lst1 = []

    for x in range(1, number+ 1):
        if number % x == 0:
            lst1.append(x)

    if len(lst1) == 2:
        return 'the number is prime {}'.format(number)
    else:
        return 'the number is composite {}'.format(number)

number = eval(input('enter a number :'))
result = prime_number(number)

print('{}'.format(result))


'''
output:  d:\pythonprogramms\prime.py(3)<module>()
-> def prime_number(number):
(Pdb) n
> d:\pythonprogramms\prime.py(16)<module>()
-> number = eval(input('enter a number :'))
(Pdb) n
enter a number :2
> d:\pythonprogramms\prime.py(17)<module>()
-> result = prime_number(number)
(Pdb) n
> d:\pythonprogramms\prime.py(19)<module>()
-> print('{}'.format(result))
(Pdb) c
the number is prime 2
'''
