#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_dig = int(str(number)[-1])
else:
    last_dig = int(str(number)[-1]) * -1

if last_dig > 5:
    end_str = 'and is greater than 5'
elif last_dig == 0:
    end_str = 'and is 0'
elif last_dig < 6 and last_dig != 0:
    end_str = 'and is less than 6 and not 0'

print(f"Last digit of {number} is {last_dig} {end_str}")
