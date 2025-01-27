
from random import *

alphabets =  "abcdefghijklmnopqrstuvwxyz"
digits = '0123456789'
cities = ['hyd','chennai','bnglr','pune','delhi','vizag']
designations = ['software engineer','sr.eng','teamlead','projectlead','projectmanager']

def get_fake_name():
    name = choice(alphabets).upper()
    n = randint(2,9)
    for x in range(n):
        name = name + choice(alphabets)
    return name

def get_fake_eno():
    eno = 'e_'
    for x in range(4):
        eno = eno +choice(digits)
    return eno

def get_fake_salary():
    esal = uniform(10000,50000)
    return esal

def get_fake_city():
    city = choice(cities)
    return city

def get_fake_mno():
    mno = choice('6789')
    for i in range(9):
        mno = mno + choice(digits)
    return mno

def get_fake_designation():
    designation = choice(designations)
    return designation

def get_fake_emp_data():
    print('employee name :',get_fake_name())
    print('employee number :',get_fake_eno())
    print('employee salary :',get_fake_salary())
    print('employee city :',get_fake_city())
    print('employee mobile number:',get_fake_mno())
    print('employee designation :',get_fake_designation())

for x in range(10):
    get_fake_emp_data()
    print('-------------------------------')

#output:
employee name : Jwvvanzze
employee number : e_2916
employee salary : 29617.261553215503
employee city : chennai
employee mobile number: 7055650589
employee designation : software engineer
-------------------------------
employee name : Juszthul
employee number : e_1644
employee salary : 43112.81067952611
employee city : chennai
employee mobile number: 6285105952
employee designation : projectlead
-------------------------------
employee name : Rkomdfrw
employee number : e_8010
employee salary : 19854.00813441169
employee city : bnglr
employee mobile number: 9557698752
employee designation : sr.eng
-------------------------------
employee name : Qlbkcreykf
employee number : e_6348
employee salary : 47779.425959868255
employee city : chennai
employee mobile number: 9410284768
employee designation : software engineer
-------------------------------
employee name : Ptpdkzyjiz
employee number : e_0401
employee salary : 35138.81983590149
employee city : delhi
employee mobile number: 9789789782
employee designation : projectmanager
-------------------------------
employee name : Fezbtep
employee number : e_7955
employee salary : 49586.69990371748
employee city : hyd
employee mobile number: 8346358943
employee designation : sr.eng
-------------------------------
employee name : Vdups
employee number : e_3913
employee salary : 34918.50930156582
employee city : delhi
employee mobile number: 6277578398
employee designation : projectlead
-------------------------------
employee name : Ccdzpnk
employee number : e_4438
employee salary : 29805.70394944739
employee city : delhi
employee mobile number: 8146644735
employee designation : software engineer
-------------------------------
employee name : Fafugaslxp
employee number : e_4958
employee salary : 16169.551598524255
employee city : vizag
employee mobile number: 8444917025
employee designation : projectlead
-------------------------------
employee name : Czilqcn
employee number : e_5036
employee salary : 29943.912334455992
employee city : delhi
employee mobile number: 7656969480
employee designation : projectlead
-------------------------------
