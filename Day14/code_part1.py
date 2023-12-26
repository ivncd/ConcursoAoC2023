with open('input.txt', 'r') as f:
    data = f.read()

data = [list(line) for line in data.strip().splitlines()]

# Inverse -y direction (Part 2)
def transformY(rows : list, inverse : bool = False) -> list:
    newArray = rows[:] # Copied array
    for columnId in range(len(newArray[0])):
        lastEmptyPosition = 0 if not inverse else len(newArray) - 1
        for rowId in range(len(newArray)):
            rowId = rowId if not inverse else len(newArray) - 1 - rowId
            if newArray[rowId][columnId] == '#':
                lastEmptyPosition = rowId + 1 if not inverse else rowId - 1
            
            elif newArray[rowId][columnId] == 'O' and (lastEmptyPosition < len(newArray) - 1 if not inverse else lastEmptyPosition > 0):
                newArray[rowId][columnId] = '.'
                newArray[lastEmptyPosition][columnId] = 'O'
                lastEmptyPosition += 1 if not inverse else -1
    
    return newArray

# Inverse -x direction (Part 2)
def transformX(rows: list, inverse : bool = False) -> list:
    newArray = rows[:] # Copied array
    for rowId in range(len(newArray)):
        lastEmptyPosition = 0 if not inverse else len(newArray[0]) - 1
        for columnId in range(len(newArray[0])):
            columnId = columnId if not inverse else len(newArray[0]) - 1 - columnId
            if newArray[rowId][columnId] == '#':
                lastEmptyPosition = columnId + 1 if not inverse else columnId - 1
            
            elif newArray[rowId][columnId] == 'O' and (lastEmptyPosition < len(newArray[0]) - 1 if not inverse else lastEmptyPosition > 0):
                newArray[rowId][columnId] = '.'
                newArray[rowId][lastEmptyPosition] = 'O'
                lastEmptyPosition += 1 if not inverse else -1
            
    return newArray


def getResult(part : list) -> int:
    result = 0
    for value, line in enumerate(part):
        result += line.count('O') * (len(part) - (value))
    
    return result


# Part 1
part1 = transformY(data)
resultPart1 = getResult(part1)

print('Part 1:', resultPart1)


"""
Part 2

cycleLength, isEqual = 1000000000, False
lastData = [[x for x in y] for y in data]

for line in lastData:
    print(''.join(line))

alreadyChecked = {}
while cycleLength > 0 or isEqual:
    part2 = [[x for x in y] for y in lastData] # No se porque deberia de funcionar [:]
    part2 = transformY(part2) # north
    part2 = transformX(part2) # west
    part2 = transformY(part2, inverse=True) # south
    part2 = transformX(part2, inverse=True) # east
    

    lastData = part2
    cycleLength -= 1


    # Check for loops because the bruteforce never ends


resultPart2 = getResult(part2)
"""


