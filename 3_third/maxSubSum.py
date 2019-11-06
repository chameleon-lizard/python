current = int(input())
fullSum = 0
maxSum = current

while current != 0:
    fullSum += current
    if fullSum > maxSum:
        maxSum = fullSum
    elif fullSum < 0:
        fullSum = 0
    current = int(input())
        
print(maxSum)
