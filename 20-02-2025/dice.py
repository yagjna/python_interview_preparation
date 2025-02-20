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
