def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return '{} likes this'.format(names[0])
    elif len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    else:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)

print(likes([]))                                
print(likes(['peter']))                        
print(likes(['jacob', 'alex']))                 
print(likes(['Max', 'John', 'Mark']))           
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))



#output:
no one likes this
peter likes this
jacob and alex like this
Max, John and Mark like this
Alex, Jacob and 2 others like this
