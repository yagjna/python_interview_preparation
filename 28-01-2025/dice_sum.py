
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1:", die1)
    print("die2",die2)
    print("Total:", die1 + die2)

roll_dice()

file_name = '28-01-2025'

with open(file_name, 'a') as fh:
    fh.write('sum of dice : \n')
    fh.write(str(roll_dice()) + '\n')

print('the file is added to - {}'.format(file_name))


#output:
Die 1: 4
die2 5
Total: 9
Die 1: 2
die2 3
Total: 5

the file is added to - 28-01-2025
