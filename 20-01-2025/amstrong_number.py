
def amstrong(num):
    temp = num
    result = 0

    while temp != 0:
        rem = temp % 10
        temp = temp // 10
        result = result + rem ** 3

    if result == num:
        return "Armstrong"
    else:
        return "Not Armstrong"

num = eval(input('enter a number :'))
result = amstrong(num)
print('{} is {}'.format(num,result))

file_name = '20-01-2025.txt'

with open(file_name, 'a')as fh:
    fh.write('\n amstrong number:\n')
    fh.write(str(result) + '\n')

print('the file is added to - {}'.format(file_name))


#output:
enter a number :153
153 is Armstrong
the file is added to - 20-01-2025.txt

enter a number :123
123 is Not Armstrong
the file is added to - 20-01-2025.txt
