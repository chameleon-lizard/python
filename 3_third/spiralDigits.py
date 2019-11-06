m, n = [int(i) for i in input().split(',')]

numbers = []
for i in range(0, m):
    numbers.append([]);
    for j in range(0, n):
        numbers[i].append(-1)

direction = 0
y = 0
x = 0
for i in range(0, m * n):
    if numbers[y][x] == -1:
        numbers[y][x] = i % 10
    
    if direction % 4 == 0:
        if y + 1 > m - 1 or numbers[y + 1][x] != -1:
            direction += 1
            x += 1
        else:
            y += 1
    elif direction % 4 == 1:
        if x + 1 > n - 1 or numbers[y][x + 1] != -1:
            direction += 1
            y -= 1
        else:
            x += 1
    elif direction % 4 == 2:
        if y - 1 < 0 or numbers[y - 1][x] != -1:
            direction += 1
            x -= 1
        else:
            y -= 1
    elif direction % 4 == 3:
        if x - 1 < 0 or numbers[y][x - 1] != -1:
            direction += 1
            y += 1
        else:
            x -= 1 
        
for i in range(0, n):
    for j in range(0, m):
        print(numbers[j][i], ' ', end='')
    print()
