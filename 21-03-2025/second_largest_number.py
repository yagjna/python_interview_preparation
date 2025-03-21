import pdb;pdb.set_trace()

def second_largest_number(lst1):

    first_largest = lst1[0]

    for x in lst1:
        if x > first_largest:
            first_largest = x

    second_largest = lst1[0]

    for y in lst1:
        if y > second_largest and y != first_largest:
            second_largest = y

    return second_largest

lst1 = [1, 2, 4, 28, 5, 8, 11]
second_largest =  second_largest_number(lst1)

print("the second largest number in the list is: {}".format(second_largest))

output:
    PS D:\pythonprogramms> & "C:/Users/Yagjna Sri B/AppData/Local/Microsoft/WindowsApps/python3.12.exe" d:/pythonprogramms/second_largest_number.py
the second largest number in the list is: 11
PS D:\pythonprogramms> & "C:/Users/Yagjna Sri B/AppData/Local/Microsoft/WindowsApps/python3.12.exe" d:/pythonprogramms/second_largest_number.py
> d:\pythonprogramms\second_largest_number.py(3)<module>()
-> def second_largest_number(lst1):
(Pdb) n
> d:\pythonprogramms\second_largest_number.py(19)<module>()
-> lst1 = [1, 2, 4, 28, 5, 8, 11]
(Pdb) n
> d:\pythonprogramms\second_largest_number.py(20)<module>()
-> second_largest =  second_largest_number(lst1)
(Pdb) print(second_largest)
*** NameError: name 'second_largest' is not defined
(Pdb) n
> d:\pythonprogramms\second_largest_number.py(22)<module>()
-> print("the second largest number in the list is: {}".format(second_largest))
(Pdb) c
the second largest number in the list is: 11

