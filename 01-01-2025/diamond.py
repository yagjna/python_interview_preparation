def diamond(size):
    if size <= 0 or size % 2 == 0:
        return None
    
    diamond_str = ""
    for i in range(1, size + 1, 2):
        spaces = " " * ((size - i) // 2)
        stars = "*" * i
        diamond_str += spaces + stars + "\n"
    
    for i in range(size - 2, 0, -2):
        spaces = " " * ((size - i) // 2)
        stars = "*" * i
        diamond_str += spaces + stars + "\n"
    
    return diamond_str


print(diamond(3))
print(diamond(5))
print(diamond(4))  

#output:
 *
***
 *

  *
 ***
*****
 ***
  *

None
