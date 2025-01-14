
# to print count of each element in the list

lst = [1, 2, 3, "a", "b", "c", "ab", "abcd", 1.2, 1.3, True, False]

import pdb;pdb.set_trace()

int_count = 0
float_count = 0
str_count = 0
bool_count = 0

for x in lst:
    if type(x) == int:
       #to count each element in the list
       int_count = int_count + 1
    elif type(x) == float:
        float_count = float_count + 1
    elif type(x) == str:
        str_count = str_count + 1
    elif type(x) == bool:
        bool_count =  bool_count + 1

print("integer count is : {}".format(int_count))
print("float coint is : {}".format(float_count))
print("string count is : {}".format(str_count))
print("bool count is : {}".format(bool_count))

#output:
integer count is : 3
float coint is : 2
string count is : 5
bool count is : 2
