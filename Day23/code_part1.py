with open('input.txt', 'r') as f:
    data = f.read()

data = data.strip().splitlines()

tile = {'^' : (0, -1), '>' : (1, 0), 'v' : (0, 1), '<' : (-1, 0)}
WIDTH, HEIGHT = len(data[0]), len(data)
start, finish = (1,0), (WIDTH - 2, HEIGHT - 1)

finalSteps = []
def traversePath(start : tuple[int, int], usedData : list[list[str]], stepsCount : int = 0, alreadyPassed = []) -> list[int]:
    x, y = start
    alIn = False
    alreadyPassed.append(start)
    possible = [(1,0), (-1,0), (0,1), (0,-1)]
    while (x,y) != finish:
        stepsCount += 1
        alreadyPassed.append((x,y))
        currentLetter = usedData[y][x]
        if currentLetter != '#':
            if currentLetter == '.':
                counter = 0
                for addX, addY in possible:
                    newX, newY = x + addX, y + addY
                    if (newX, newY) not in alreadyPassed and 0 <= newX < WIDTH and 0 <= newY < HEIGHT:
                        if usedData[newY][newX] != '#':
                            if counter == 0:
                                currentX, currentY = newX, newY
                            else:
                                traversePath((newX, newY), usedData, stepsCount, alreadyPassed[:])
                            
                            counter += 1
                
                x, y = currentX, currentY
            
            else:
                addX, addY = tile[currentLetter]
                x, y = x + addX, y + addY
        
        if (x,y) in alreadyPassed:
            alIn = True
            break

    if not alIn:
        finalSteps.append(stepsCount)



traversePath(start=start, usedData = data)
print('Part 1:', max(finalSteps)) # 2074


# Part 2 - Bruteforce - Never ends
"""
newData = []
for y, line in enumerate(data):
    newData.append([])
    for x, letter in enumerate(line):
        letter = letter if letter in ('.', '#') else '.'
        newData[y].append(letter)

finalSteps = []
traversePath(start=start, usedData=newData, p2=True, alreadyPassed=[])
print('Part 2:', max(finalSteps))
"""