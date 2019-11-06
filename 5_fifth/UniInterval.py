intervals = eval(input())

a = [(left, True) for left, right in intervals]
a += [(right, False) for left, right in intervals]

a.sort()

counter = 0
result = 0

for i, current in enumerate(a):
    if i > 0 and counter > 0:
        result += abs(a[i][0] - a[i-1][0])
    else:
        result += 0
    if current[1]:
        counter += 1
    else:
        counter -= 1

print(result)
