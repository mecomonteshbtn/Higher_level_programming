#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if abs(number) % 10 > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, abs(number) % 10))
elif abs(number) % 10 == 0:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, abs(number) % 10))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, abs(number) % 10))
