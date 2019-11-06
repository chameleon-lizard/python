from math import *

func = input()
A, B = input().split(",")
A, B = float(A), float(B)
mid = (A + B) / 2
x = mid

while (B - A) / 2 >= 0.000001:
    mid = (A + B) / 2
    x = mid
    mid_test = eval(func)
    x = A
    left_test = eval(func)
    if mid_test * left_test > 0:
        A = mid
    else:
        B = mid

print((A + B) / 2)
