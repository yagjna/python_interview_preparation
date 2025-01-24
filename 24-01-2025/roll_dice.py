
import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Die 1:", die1)
    print("die2",die2)
    print("Total:", die1 + die2)

roll_dice()

#output:
Die 1: 1
die2 6
Total: 7
