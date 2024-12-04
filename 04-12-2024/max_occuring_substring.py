def max(lst1):

    dict1 = {}

    for x in lst1:
        if x in dict1:
            dict1[x] = dict1[x] +1
        else:
            dict1[x] =1

    for k,v in dict1.items():
        if v > 1:
            print(k)


lst1 = ['this', 'is', 'python', 'python', 'is', 'good']
max(lst1)



#output: 
is
python
