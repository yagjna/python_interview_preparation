def interchange(lst1):
    lst1[0] , lst1[-1]= lst1[-1], lst1[0]
   
    print(lst1)
lst1 =[1,2,3,4,5]
interchange(lst1)



output:
    [5, 2, 3, 4, 1]
