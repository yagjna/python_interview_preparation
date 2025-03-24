
import pdb;pdb.set_trace()

def fabnocci_series(num):

    a, b = 0, 1

    lst1 = []

    for x in range(num):
        lst1.append(a)

        a, b = b, a + b

    return lst1

num = eval(input('enter a number : '))
print(fabnocci_series(num))

'''
output: -> def fabnocci_series(num):
(Pdb) n
> d:\pythonprogramms\fabnocci_series.py(16)<module>()
-> num = eval(input('enter a number : '))
(Pdb) 5
5
(Pdb) n
enter a number : 5
> d:\pythonprogramms\fabnocci_series.py(17)<module>()
-> print(fabnocci_series(num))
(Pdb) c
[0, 1, 1, 2, 3]
PS D:\pythonprogramms>
'''
