def words_to_marks(s):
    total = 0
    for x in s:
        total = total + ord(x) - ord('a')+1
        
    return total
s = 'love'
print(words_to_marks(s))

s = 'yagjna'
print(words_to_marks(s))

s = 'friendship'
print(words_to_marks(s))

#output:
54
58
108
