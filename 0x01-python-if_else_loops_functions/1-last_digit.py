#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print("The Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("The last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))
else:
    print("The last digit of {:d} is 0 and is 0".format(number))
