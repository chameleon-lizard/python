from math import *
from sys import exit

number = int(input())
length = floor(log(number, 10))

if number % 10 == 0:
    print("NO")
    exit()

left_divisor = 10**length
right_divisor = 10

while left_divisor >= right_divisor:
    left_digit = number // left_divisor - 10 * (number // (left_divisor * 10))
    right_digit = (number % right_divisor - number % (right_divisor // 10)) // (right_divisor // 10)
    if left_digit != right_digit:
        print("NO")
        break
    else:
        left_divisor //= 10
        right_divisor *= 10
else:
    print("YES") 
