def solution(s):
    lst1 = []
    
    if len(s) % 2 != 0:
        s = s + '_'

    for i in range(0, len(s), 2):
        lst1.append(s[i:i+2])
    
    return lst1


print(solution('abc'))  
print(solution('abcdef'))  
print(solution('a')) 
print(solution('12345'))  


#output:
['ab', 'c_']
['ab', 'cd', 'ef']
['a_']
['12', '34', '5_']
