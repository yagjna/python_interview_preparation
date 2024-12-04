
def count(str1):

    dict1 = {}
    str2  =str1.split(' ')
    
    for x in str2:
        if x in dict1:
            dict1[x] = dict1[x] +1
        else:
            dict1[x] = 1
    for k,v in dict1.items():
        dict1[k] = v
        print(k,v)

str1 = eval(input('enter a string : '))
count(str1)


#output:
enter a string : 'hello world python'
hello 1
world 1
python 1


enter a string : "hello world! how r u world?"
hello 1
world! 1
how 1
r 1
u 1
world? 1
