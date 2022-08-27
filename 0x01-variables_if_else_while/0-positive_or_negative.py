import random

def pos_neg():
    n = (random.randint(-100,100))
    if n > 0:
        print(str(n) + ' is positive')
    elif n == 0:
        print(str(n) + ' is zero')
    else:
        print(str(n) + ' is negative')
pos_neg()

