
from random import *

def otp(digits):
    otp = ''
    for x in range(6):
        otp = otp + choice(digits)
    return otp

digits = "1234567890"
otp = otp(digits)
print('the otp is: {}'.format(otp))

file_name = 'otp.txt'

with open(file_name, 'w') as fh:
    fh.write('the otp is : {}\n'.format(otp))

print('the otp is saved to {}'.format(file_name))

