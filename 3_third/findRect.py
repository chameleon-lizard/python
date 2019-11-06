buf = ''
battlemap = []
buf = input()
flag = 0

while buf[0] != '-' or flag == 0:
    battlemap.append(buf)
    buf = input()
    flag += 1
    
count = 0
x_length = battlemap[0].__len__() - 1
y_length = battlemap.__len__()
for i in range(1, x_length):
    for j in range(0, y_length):
        if (
            battlemap[j][i] == '#' and \
            (battlemap[j - 1][i] == '-' or battlemap[j - 1][i] == '.') and \
            (battlemap[j][i - 1] == '-' or battlemap[j][i - 1] == '.') and \
            (battlemap[j - 1][i - 1] == '-' or battlemap[j - 1][i - 1] == '.') \
            ):
            count += 1
            
print(count)
