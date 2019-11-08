def turtle(coord, direction):      
    while True:
        command = yield coord
        if command == 'f':
            if direction == 0:
                coord = (coord[0] + 1, coord[1])
            elif direction == 1:
                coord = (coord[0], coord[1] + 1)
            elif direction == 2:
                coord = (coord[0] - 1, coord[1])
            else:
                coord = (coord[0], coord[1] - 1)
        elif command == 'r':
            direction = (direction - 1) % 4
        elif command == 'l':
            direction = (direction + 1) % 4