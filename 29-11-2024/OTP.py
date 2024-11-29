from random import *
def otp(digits):
    otp = ''
    for x in range(6):
        otp = otp + choice(digits)
    return otp
digits = "1234567890"
otp = otp(digits)
print(otp)




output:
970647
241420

