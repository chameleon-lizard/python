dungeon = {}

while True:
    tunnels = input().split()

    if len(tunnels) == 1:
        enter = tunnels[0]
        exit = input()
        break

    if tunnels[0] in dungeon:
        dungeon[tunnels[0]].append(tunnels[1])
    else:
        dungeon[tunnels[0]] = []
        dungeon[tunnels[0]].append(tunnels[1])

    if tunnels[1] in dungeon:
        dungeon[tunnels[1]].append(tunnels[0])
    else:
        dungeon[tunnels[1]] = []
        dungeon[tunnels[1]].append(tunnels[0])

visited = set()
stack = []
stack.append(enter)

for i in stack:
    visited.add(i)

    for j in dungeon[i]:
        if j not in visited:
            stack.append(j)

print("YES") if exit in visited else print("NO")