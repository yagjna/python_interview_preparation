#Write a Python program to swap two numbers without using a temporary variable.
import pdb;pdb.set_trace()
def swapping_of_two_numbers(a, b):

    temp = a
    a = b
    b = temp

    return a, b

a = eval(input('enter first number : '))
b = eval(input('enter second number :'))

a, b = swapping_of_two_numbers(a, b)

numb1 = print('a ={} '.format(a))
numb2 = print('b = {}'.format(b))

''' 
output: -> def swapping_of_two_numbers(a, b):
(Pdb) n
> d:\pythonprogramms\swapping_using_temp.py(11)<module>()
-> a = eval(input('enter first number : '))
(Pdb) a = 1
(Pdb) b = 2
*** The specified object '= 2' is not a function or was not found along sys.path.
(Pdb) n
enter first number : 1
> d:\pythonprogramms\swapping_using_temp.py(12)<module>()
-> b = eval(input('enter second number :'))
(Pdb) n
enter second number :2
> d:\pythonprogramms\swapping_using_temp.py(14)<module>()
-> a, b = swapping_of_two_numbers(a, b)
(Pdb) a
(Pdb) b
(Pdb) print(a)
1
(Pdb) print(b)
2
(Pdb) n
> d:\pythonprogramms\swapping_using_temp.py(16)<module>()
-> numb1 = print('a ={} '.format(a))
(Pdb) c
a =2 
b = 1


'''
