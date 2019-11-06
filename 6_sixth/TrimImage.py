# Input
rects = []
some = input().split()
rects.append(
        (
            min(int(some[0]), int(some[0]) + int(some[2])), 
            max(int(some[0]), int(some[0]) + int(some[2])), 
            min(int(some[1]), int(some[1]) + int(some[3])), 
            max(int(some[1]), int(some[1]) + int(some[3])),
            some[4]
            )
        )
xmin, xmax, ymin, ymax = rects[0][0], rects[0][1], rects[0][2], rects[0][3]

while True:
    some = input().split()
    if some[0] == '0' and some[1] == '0' and some[2] == '0' and some[3] == '0':
        break
    if some[2] == '0' or some[3] == '0':
        continue
    rects.append(
            (
                min(int(some[0]), int(some[0]) + int(some[2])), 
                max(int(some[0]), int(some[0]) + int(some[2])), 
                min(int(some[1]), int(some[1]) + int(some[3])), 
                max(int(some[1]), int(some[1]) + int(some[3])),
                some[4]
                )
            )
    if xmin > rects[-1][0]:
        xmin = rects[-1][0]
    if xmax < rects[-1][1]:
        xmax = rects[-1][1]
    if ymin > rects[-1][2]:
        ymin = rects[-1][2]
    if ymax < rects[-1][3]:
        ymax = rects[-1][3]

width = abs(xmax - xmin)
height = abs(ymax - ymin)
# Creating canvas
canvas = [['.']*(width) for i in range(height)]

for rect in rects:
    for i in range(rect[0], rect[1]):
        for j in range(rect[2], rect[3]):
            canvas[j - ymax][i - xmax] = rect[4]

for j in range(height):
    for i in range(width):
        print(canvas[j][i], end = '')
    print()
