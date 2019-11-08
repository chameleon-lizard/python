def turtle(coord, direction):      
    command = yield coord

    if command == f:
        coord[direction % 2] += (direction % 2) * (-1)
    elif command == r:
        direction = (direction - 1) % 4
    elif command == l:
        direction = (direction + 1) % 4