def find_next_square(sq):
    if (sq ** 0.5).is_integer():
        root = int(sq ** 0.5)
        return (root + 1) ** 2
    else:
        return -1
    
sq = 121
print(find_next_square(sq))

sq = 123
print(find_next_square(sq))


#output:
144
-1
