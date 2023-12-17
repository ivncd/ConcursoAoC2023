with open('input.txt', 'r') as f:
    data = f.read()


data = data.strip().splitlines()
WIDTH, HEIGHT = len(data[0]), len(data)
def lightBeam(start, currentDirection, ENERGYZED_POINTS, n=0, alreadyUsedX=[], alreadyUsedY=[]):
    x, y = start
    outOfBounds = False
    while not outOfBounds:
        if x < WIDTH and x >= 0 and y < HEIGHT and y >= 0:
            if (x,y) in alreadyUsedY or (x,y) in alreadyUsedX: #Don't follow the loop in case we encounter a loop
                break

            letter = data[y][x]
            #print(f'[{n}]', x, y, letter)

            if letter != '.':
                if letter == '\\':
                    currentDirection = (0, currentDirection[0]) if currentDirection[1] == 0 else (currentDirection[1], 0)

                elif letter == '/':
                    currentDirection = (0, -currentDirection[0]) if currentDirection[1] == 0 else (-currentDirection[1], 0)
                
                elif letter == '|':
                    if currentDirection[1] == 0:
                        alreadyUsedX.append((x,y))

                        lightBeam((x,y - 1), (0, -1), ENERGYZED_POINTS, n+1, alreadyUsedX=alreadyUsedX, alreadyUsedY=alreadyUsedY)
                        currentDirection = (0, 1)
                    
                elif letter == '-':
                    if currentDirection[0] == 0:
                        alreadyUsedY.append((x,y))

                        lightBeam((x - 1, y), (-1, 0), ENERGYZED_POINTS, n+1, alreadyUsedX=alreadyUsedX, alreadyUsedY=alreadyUsedY)
                        currentDirection = (1, 0)
                        

            if (x,y) not in ENERGYZED_POINTS:
                ENERGYZED_POINTS[(x,y)] = 1
            else:
                ENERGYZED_POINTS[(x,y)] += 1

            x, y = x + currentDirection[0], y + currentDirection[1]

        else:
            break
        

# Part 1
ePoints = {}
lightBeam(start=(0,0), currentDirection=(1,0), ENERGYZED_POINTS=ePoints, alreadyUsedX=[], alreadyUsedY=[])


# Part 2
currentHighest = 0
for y in range(HEIGHT):
    for x in range(0, WIDTH) if y in (0, HEIGHT - 1) else (0, -1):
        ePoints2 = {}
        directions = []

        if x == -1 or x == WIDTH - 1:
            directions.append((-1, 0))
        
        elif x == 0:
            directions.append((1, 0))

        if y == 0:
            directions.append((0, 1))

        elif y == HEIGHT - 1:
            directions.append((0, -1))
        

        for direction in directions:
            ePoints2 = {}
            lightBeam(start=(x,y), currentDirection=direction, ENERGYZED_POINTS=ePoints2, alreadyUsedX=[], alreadyUsedY=[])

            if len(ePoints2) > currentHighest:
                currentHighest = len(ePoints2)
    


print('Part 1:', len(ePoints)) # 6514
print('Part 2', currentHighest)

    