from math import sqrt

def distance(x1, y1, z1, x2, y2, z2):
    return sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2 + abs(z1 - z2)**2)

galaxy = []

while True:
    buff = input().split()
    if len(buff) == 1:
        break
    galaxy.append((float(buff[0]), float(buff[1]), float(buff[2]), buff[3]))
    
a = ""
b = ""
dist = 0

for i in range(len(galaxy)):
    for j in range(i+1, len(galaxy)):
        current = distance(galaxy[i][0], galaxy[i][1], galaxy[i][2], galaxy[j][0], galaxy[j][1], galaxy[j][2])
        if current > dist:
            dist = current
            a = galaxy[i][3]
            b = galaxy[j][3]

if a < b:
    print(a, b)
else:
    print(b, a)