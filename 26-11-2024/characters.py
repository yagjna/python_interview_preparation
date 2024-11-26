# to take a string statically and to find sum of int,float,char

lst1 = [1, 2, 3, "a", "b", "c", 1.2, 1.3, 1.4, "d", "e", "f", True, False]

import pdb;pdb.set_trace()

sum_int = 0
sum_float = 0
string_con = ""
bool_list = []

for x in lst1:
    if type(x) == int:
        sum_int = sum_int + x 
    elif type(x) == float:
        sum_float = sum_float + x
    elif type(x) == str:
       import pdb;pdb.set_trace()
       string_con = string_con + x
    elif type(x) == bool:
        bool_list.append(x)

print("the sum of integer numbers is {}".format(sum_int))
print("the sum float numbers is {}".format(sum_float))
print("the string is {}".format(string_con))
print("the list of bool is {}".format(bool_list))



output:the sum of integer numbers is 6
the sum float numbers is 3.9
the string is abcdef
the list of bool is [True, False]
