
import pdb;pdb.set_trace()
def factorial(number):

    fact = 1

    for x in range(1, number+ 1):

        fact = fact * x

    return fact

number = eval(input('enter a number :'))
fact =  factorial(number)

print('the factorial of the number is - {}'.format(fact))

"""
output:  def factorial(number):
(Pdb) n
> d:\pythonprogramms\factoroial.py(12)<module>()
-> number = eval(input('enter a number :'))
(Pdb) number = 5
(Pdb) n
enter a number :5
> d:\pythonprogramms\factoroial.py(13)<module>()
-> fact =  factorial(number)
(Pdb) c
the factorial of the number is - 120
"""
