#sum of all num in  a given range
# sum = 0

# for x in range(100,200):
#     sum = sum + x

# print("the sum of numbers in the range of 100,200 is {}".format(sum))

import pdb; pdb.set_trace()

a = int(input("enter a number: "))
b = int(input("enetr a number: "))

sum = 0

if a < b and a > 0 or b > 0:
 for x in range(a, b+1):
    sum = sum + x

 print(" the sum of {} and {}  is {}".format(a, b, sum))
else:
  print("unable to find the sum with range {}, {}".format(a, b))


