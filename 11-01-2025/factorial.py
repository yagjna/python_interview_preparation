
number = int(input("enter a number : "))
import pdb;pdb.set_trace()

#assuming the intiail factorial of a number is 1
factorial = 1

for x in range(1,number+1):
    factorial = factorial * x

print(factorial)

#output:
enter a number : 5
> d:\pythonprogramms\factorial.py(5)<module>()
-> factorial = 1
(Pdb) c
120
