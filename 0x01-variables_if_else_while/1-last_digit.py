import random

def lastDigit(n):
    num = n%10
    if num > 5:
        print('Last digit of ' + str(n) + ' is ' + str(num) + ' and is greater than 5')
    elif num == 0:
        print('Last digit of ' + str(n) + ' is ' + str(num) + ' and is 0')
    elif num < 6 and  num != 0:
        print('Last digit of ' + str(n) + ' is ' + str(num) + ' and is less than 6 and not 0')

spam = random.randint(2375, 348659)
lastDigit(spam)


