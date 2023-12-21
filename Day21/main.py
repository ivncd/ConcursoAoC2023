with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

startPosition = (0,0)
for y in range(len(data)):
    if 'S' in data[y]:
        startPosition = (data[y].index('S'), y)
        break


WIDTH, HEIGHT = len(data[0]), len(data)
def getPossibleSteps(positions: list[tuple[int, int]], maxSteps : int, part2 : bool = False):
    possibleAdd, steps = [(0,1), (0,-1), (1,0), (-1, 0)], 1
    while steps <= maxSteps:
        newPositions = []
        for x, y in positions:
            for addX, addY in possibleAdd:
                newX, newY = x + addX, y + addY
                if part2:
                    rX, rY = newX, newY
                    newX, newY = newX % WIDTH, newY % HEIGHT

                if ((newX, newY) if not part2 else (rX, rY)) not in newPositions and 0 <= newX < WIDTH and 0 <= newY < HEIGHT:
                    if data[newY][newX] != '#':
                        newPositions.append((newX, newY) if not part2 else (rX, rY))
        
        positions = newPositions
        steps += 1

    return len(positions)

resultPart1 = getPossibleSteps([startPosition], 64)
print('Part 1:', resultPart1) # 3743

# Not possible bruteforce
# resultPart2 = getPossibleSteps([startPosition], 26501365, part2=True)
# print('Part 2:', resultPart2)


"""
Idea for part2:
Calculate starting from the border and create a map in each border coordinates and just start first and then follow the border probably
 - Difficult to do just because some of them just stay still moving -> <- repeatedly
"""