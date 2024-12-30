def find_short(s):
    str1 = s.split(' ')
    shortest = s[0]
    
    for x in str1:
        if x < shortest:
            shortest = x
            
    return len(shortest)

s = 'string of words'
len = find_short(s)
print('the shortest word length is - {}'.format(len))


#output:
the shortest word length is - 2
