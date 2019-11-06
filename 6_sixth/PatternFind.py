def isPresent(string, substring, j):
    for i in range(len(substring)):
        if substring[i] == '@':
            continue
        elif string[i+j] != substring[i]:
            return i
    return -1

string = input()
substring = input()

count = 0
for i in substring:
    if i == '@':
        count += 1
    else:
        break

i = 0
while i <= len(string) - len(substring):
    ret = isPresent(string, substring, i)
    if ret == -1:
        print(i)
        break
    else:
        i += ret + 1 - count
else:
    print('-1')
