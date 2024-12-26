def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

year = 2016
print(is_leap_year(year)) 

year = 2018
print(is_leap_year(year)) 

year = 4000
print(is_leap_year(year)) 


#output:
True
False
True
